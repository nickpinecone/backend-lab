using NServiceBus;

namespace Messages;

public class UpdateStudents : ICommand
{
    public int StudentCount { get; set; }
}
