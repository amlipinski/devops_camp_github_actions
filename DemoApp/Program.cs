var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", () => "Hello World, you are now running on Azure WebApp!!");

app.Run();
