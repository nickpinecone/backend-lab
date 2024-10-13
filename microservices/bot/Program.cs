using System;
using System.Net.Http;
using System.Threading;
using System.Threading.Tasks;
using Telegram.Bot;
using Telegram.Bot.Polling;
using Telegram.Bot.Types;
using Telegram.Bot.Types.Enums;

namespace Bot;

public static class Program
{
    static TelegramBotClient _bot = null;
    static HttpClient _http = null;

    public static async Task Main(string[] args)
    {
        _http = new HttpClient() {
            BaseAddress = new Uri("http://core:5000"),
        };

        using var cts = new CancellationTokenSource();

        var bot = new TelegramBotClient("6414959440:AAFj-6QdyQx30CF1ArxqMdd2nRVblO4Jex4", cancellationToken: cts.Token);
        _bot = bot;

        var me = await bot.GetMeAsync();

        bot.OnError += OnError;
        bot.OnMessage += OnMessage;

        Console.WriteLine($"@{me.Username} is running... Press Enter to terminate");
        while (true)
        {
        }

        cts.Cancel();
    }

    static async Task OnMessage(Message msg, UpdateType type)
    {
        if (msg.Text == "/start")
        {
            await _bot.SendTextMessageAsync(msg.Chat, "Привет!");
        }
        else if (msg.Text == "/auth")
        {
            await _http.GetAsync("addStudent");
            await _bot.SendTextMessageAsync(msg.Chat, "Авторизация успешна!");
        }
    }

    static async Task OnError(Exception exception, HandleErrorSource source)
    {
        Console.WriteLine(exception);
    }
}
