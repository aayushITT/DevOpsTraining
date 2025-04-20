using Microsoft.AspNetCore.Mvc;

namespace MyDotNetApp.Controllers
{
    public class HomeController : Controller
    {
        public IActionResult Index()
        {
            return Content("Hello, this is your web page!");
        }
    }
}

