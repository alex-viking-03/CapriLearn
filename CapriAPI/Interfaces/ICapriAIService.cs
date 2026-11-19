namespace CapriAPI.Interfaces
{
    public interface ICapriAIService
    {
        Task<string> AskAsync(string message);
    }
}
