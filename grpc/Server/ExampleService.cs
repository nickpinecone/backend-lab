using System.Threading.Tasks;
using Grpc.Core;

namespace GrpcExample;

public class ExampleService : Example.ExampleBase
{
    public override Task<ExampleReply> ExampleMethod(ExampleRequest request, ServerCallContext context)
    {
        return Task.FromResult(new ExampleReply
        {
            Message = $"Hello, {request.Name}!"
        });
    }
}