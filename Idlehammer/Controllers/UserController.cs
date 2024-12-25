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
}
