# Use the official .NET SDK image to build the app
# Use the official .NET SDK image that supports .NET 8.0 (if available)
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build


# Set the working directory inside the container
WORKDIR /app

# Copy the project file(s) and restore any dependencies (via `dotnet restore`)
COPY *.csproj ./
RUN dotnet restore

# Copy the rest of the application source code and build the application
COPY . ./
RUN dotnet publish -c Release -o /app/publish

# Use the official .NET runtime image to run the app
FROM mcr.microsoft.com/dotnet/aspnet:7.0 AS runtime

# Set the working directory in the runtime image
WORKDIR /app

# Copy the published app from the build stage
COPY --from=build /app/publish .

# Expose the port the app will run on (optional)
EXPOSE 5000

# Define the entry point for the app
ENTRYPOINT ["dotnet", "MyDotNetApp.dll"]

