using System.Diagnostics.Contracts;

namespace CapriAPI.DTO
{
    public class ResponseDTO
    {
        public string ConversationId { get; set; } = string.Empty;
        public string Type {  get; set; } = "chat";
        public string Content { get; set; } = string.Empty;
    }
}
