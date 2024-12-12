using AutoMapper;
using CSharpClicker.Web.DomainServices;
using CSharpClicker.Web.Infrastructure.Abstractions;
using CSharpClicker.Web.UseCases.Common;
using CSharpClicker.Web.UseCases.GetCurrentUser;
using CSharpClicker.Web.UseCases.GetLeaderboard;
using CSharpClicker.Web.UseCases.GetUserSettings;
using CSharpClicker.Web.UseCases.SetUserAvatar;
using MediatR;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace CSharpClicker.Web.Controllers;

[Route("user")]
[Authorize]
public class UserController : Controller
{
    private readonly IMediator mediator;
    private readonly ICurrentUserAccessor currentUserAccessor;
    private readonly IAppDbContext appDbContext;
    private IMapper mapper;

    public UserController(IMediator mediator, ICurrentUserAccessor currentUserAccessor, IAppDbContext appDbContext,
                          IMapper mapper)
    {
        this.mediator = mediator;
        this.currentUserAccessor = currentUserAccessor;
        this.appDbContext = appDbContext;
        this.mapper = mapper;
    }

    [HttpPost("avatar")]
    public async Task<IActionResult> SetAvatar(SetUserAvatarCommand command)
    {
        await mediator.Send(command);

        return RedirectToAction("Settings", "User");
    }

    [HttpGet("leaderboard")]
    public async Task<IActionResult> Leaderboard(GetLeaderboardQuery query)
    {
        var leaderboard = await mediator.Send(query);

        return View(leaderboard);
    }

    public async Task<IActionResult> Settings()
    {
        var userSettings = await mediator.Send(new GetCurrentUserSettingsQuery());

        return View(userSettings);
    }

    [HttpGet("boosts")]
    public async Task<IResult> GetUserBoosts(CancellationToken cancellationToken)
    {
        var userId = currentUserAccessor.GetCurrentUserId();
        var user = await appDbContext.ApplicationUsers.Include(user => user.UserBoosts)
                       .ThenInclude(ub => ub.Boost)
                       .FirstAsync(user => user.Id == userId, cancellationToken);

        var dtos = new List<UserBoostDto>();

        foreach (var boost in user.UserBoosts)
        {
            dtos.Add(mapper.Map<UserBoostDto>(boost));
        }

        return Results.Ok(dtos);
    }

    [HttpPost("boost/super")]
    public async Task<IResult> SuperAttack(Guid boostId, CancellationToken cancellationToken)
    {
        var userId = currentUserAccessor.GetCurrentUserId();
        var user = await appDbContext.ApplicationUsers.Include(user => user.UserBoosts)
                       .ThenInclude(ub => ub.Boost)
                       .FirstAsync(user => user.Id == userId, cancellationToken);

        var boost = user.UserBoosts.FirstOrDefault(ub => ub.Id == boostId);

        if (boost == null || boost.CurrentCharge < boost.Boost.MaxCharge)
        {
            throw new Exception("Could not active the super");
        }

        boost.CurrentCharge = 0;
        user.CurrentScore += boost.Boost.Profit * 10;

        if (user.CurrentScore > user.RecordScore)
        {
            user.RecordScore = user.CurrentScore;
        }

        var profitPerSecond = user.UserBoosts.GetProfit(shouldCalculateAutoBoosts: true);
        var profitPerClick = user.UserBoosts.GetProfit();

        await appDbContext.SaveChangesAsync(cancellationToken);

        return Results.Ok(new ScoreDto()
        {
            CurrentScore = user.CurrentScore,
            RecordScore = user.RecordScore,
            ProfitPerClick = profitPerClick,
            ProfitPerSecond = profitPerSecond,
        });
    }

    [HttpPost("boost/charge")]
    public async Task<IResult> ChargeBoosts(CancellationToken cancellationToken)
    {
        var userId = currentUserAccessor.GetCurrentUserId();
        var user = await appDbContext.ApplicationUsers.Include(user => user.UserBoosts)
                       .ThenInclude(ub => ub.Boost)
                       .FirstAsync(user => user.Id == userId);

        foreach (var boost in user.UserBoosts)
        {
            boost.CurrentCharge += 1;

            if (boost.CurrentCharge >= boost.Boost.MaxCharge)
            {
                boost.CurrentCharge = boost.Boost.MaxCharge;
            }
        }

        await appDbContext.SaveChangesAsync(cancellationToken);

        return Results.Ok();
    }
}
