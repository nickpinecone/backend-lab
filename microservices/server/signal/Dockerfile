FROM ubuntu

RUN apt-get update -yqq && apt-get upgrade -yqq
RUN apt-get install -yqq dotnet-sdk-8.0
RUN apt-get install -yqq aspnetcore-runtime-8.0

ADD ./signal /opt/signal
ADD ./messages /opt/messages
WORKDIR /opt/signal
RUN dotnet restore

EXPOSE 5002

CMD ["dotnet", "run"]
