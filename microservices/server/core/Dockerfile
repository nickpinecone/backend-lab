FROM ubuntu

RUN apt-get update -yqq && apt-get upgrade -yqq
RUN apt-get install -yqq dotnet-sdk-8.0
RUN apt-get install -yqq aspnetcore-runtime-8.0

ADD . /opt/core
WORKDIR /opt/core
RUN dotnet restore

EXPOSE 5000

CMD ["dotnet", "run"]
