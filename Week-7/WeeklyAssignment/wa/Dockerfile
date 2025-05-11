# dotnet sdk as base image
FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build

# app as working directory
WORKDIR /app

# Copy .csproj files inside app folder
COPY *.csproj ./

# Required packages from csprog files are downloaded and made avaialable
RUN dotnet restore

# Copy all files of dotnet to app folder
COPY . ./

# Publish the application
RUN dotnet publish -c Release -o out
# builds the .NET Core Web API Application in Release mode and publishes the output to the out directory.


# aspnet as base image for providing runtime to run .net core application
FROM mcr.microsoft.com/dotnet/aspnet:6.0

# same app as working directory
WORKDIR /app

# copy the compiled application from build component to current runtime component
COPY --from=build /app/out ./

# expose the container to port 80
EXPOSE 80

ENTRYPOINT ["dotnet"]

CMD ["HelloWorldApp.dll"]
