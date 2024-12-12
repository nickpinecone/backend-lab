namespace CSharpClicker.Web.UseCases.GetCurrentUser;

public class UserBoostDto
{
    public Guid Id { get; set; }

    public int BoostId { get; init; }

    public long CurrentPrice { get; init; }

    public int Quantity { get; init; }

    public int CurrentCharge { get; init; }
}
