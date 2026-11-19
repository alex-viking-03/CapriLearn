using CapriAPI.Interfaces;
using System.Runtime.CompilerServices;

namespace CapriAPI.Services
{
    public class CapriAIService: ICapriAIService
    {
        private readonly HttpClient _httpClient;
        public CapriAIService(HttpClient httpClient)
        {
            _httpClient = httpClient;
        }

        public async Task<string> AskAsinc(string message)
        {
            var request = new
            {
                message = message
            };

            var httpResponse = await _httpClient.PostAsJsonAsync("/chat", request);

            httpResponse.EnsureSuccessStatusCode();

            var response = await httpResponse.Content.ReadFromJsonAsync<PythonAIResponse>();

            return response?.Answer ?? throw new Exception("PythonAI вернул пустой ответ");
        }

        private class PythonAIResponse
        {
            public string Answer { get; set; } = string.Empty;
        }
    }
}
