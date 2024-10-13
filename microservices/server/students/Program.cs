using System.Linq;
using System.Threading.Tasks;
using Messages;
using Microsoft.AspNetCore.Builder;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using NServiceBus;

namespace Students;

public static class Program
{
    public static async Task Main(string[] args)
    {
        var builder = WebApplication.CreateBuilder(args);

        var connection = builder.Configuration.GetConnectionString("Database");
        builder.Services.AddDbContext<StudentDb>(options => options.UseNpgsql(connection));

        var app = builder.Build();

        using (var scope = app.Services.CreateScope())
        {
            var services = scope.ServiceProvider;

            var context = services.GetRequiredService<StudentDb>();
            if (context.Database.GetPendingMigrations().Any())
            {
                context.Database.Migrate();
            }
        }

        var endpointConfiguration = new EndpointConfiguration("Students");
        endpointConfiguration.EnableInstallers();
        endpointConfiguration.UseSerialization<SystemJsonSerializer>();

        var transport = endpointConfiguration.UseTransport<RabbitMQTransport>();
        transport.UseConventionalRoutingTopology(QueueType.Quorum);
        transport.ConnectionString("host=mq");

        var routing = transport.Routing();
        routing.RouteToEndpoint(typeof(UpdateStudents), "Signal");

        var endpointInstance = await NServiceBus.Endpoint.Start(endpointConfiguration);

        app.MapGet("/students", (StudentDb db) => db.Students.Count());
        app.MapGet("/addStudent",
                   async (StudentDb db) =>
                   {
                       db.Students.Add(new Student());

                       await db.SaveChangesAsync();
                       await endpointInstance.Send(new UpdateStudents() { StudentCount = db.Students.Count() });

                       return db.Students.Count();
                   });

        app.Run();

        await endpointInstance.Stop();
    }

    public class StudentDb : DbContext
    {
        public DbSet<Student> Students => Set<Student>();

        public StudentDb(DbContextOptions<StudentDb> options) : base(options)
        {
        }
    }

    public class Student
    {
        public int Id { get; set; }
    }
}
