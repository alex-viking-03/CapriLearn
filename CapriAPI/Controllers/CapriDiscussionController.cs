using CapriAPI.DTO;
using CapriAPI.Interface;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace CapriAPI.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class CapriDiscussionController : ControllerBase
    {
        private readonly ICapriAIService _capriAIService;

        public CapriDiscussionController(ICapriAIService capriAIService)
        {
            _capriAIService = capriAIService;
        }

        [HttpPost("messages")]
        public async Task<IActionResult> SendMessage([FromBody] RequestDTO request)
        {
            if (string.IsNullOrWhiteSpace(request.Message))
            {
                return BadRequest("Message can't be empty");
            }

            string answer = await _capriAIService.AskAsync(request.Message);

            var response = new ResponseDTO
            {
                ConversationId = request.ConversationId ?? Guid.NewGuid().ToString(),
                Type = "chat",
                Content = answer
            };

            return Ok(response);
        }
    }
}
