FROM ubuntu

RUN apt-get update -yqq && apt-get upgrade -yqq
RUN apt-get install -yqq dotnet-sdk-8.0
RUN apt-get install -yqq aspnetcore-runtime-8.0

ADD ./students /opt/students
ADD ./messages /opt/messages
WORKDIR /opt/students
RUN dotnet restore

EXPOSE 5001

CMD ["dotnet", "run"]
