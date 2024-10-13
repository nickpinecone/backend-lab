FROM ubuntu

RUN apt-get update -yqq && apt-get upgrade -yqq
RUN apt-get install -yqq dotnet-sdk-8.0
RUN apt-get install -yqq aspnetcore-runtime-8.0
RUN dotnet nuget add source https://pkgs.dev.azure.com/tgbots/Telegram.Bot/_packaging/release/nuget/v3/index.json -n Telegram.Bot

ADD . /opt/bot
WORKDIR /opt/bot
RUN dotnet restore

CMD ["dotnet", "run"]
