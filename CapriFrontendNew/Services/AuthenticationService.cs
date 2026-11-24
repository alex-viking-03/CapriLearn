using CapriFrontendNew.Models.Authentication;

namespace CapriFrontendNew.Services
{
    public class AuthenticationService
    {
        private readonly ApiClient _apiClient;

        public AuthenticationService(ApiClient apiClient)
        {
            _apiClient = apiClient;
        }

        public async Task<UserResponse?> RegisterAsync(RegisterRequest request)
        {
            return await _apiClient.PostAsync<RegisterRequest, UserResponse>("api/users/register", request);
        }

        public async Task<UserResponse?> LoginAsync(LoginRequest request)
        {
            return await _apiClient.PostAsync<LoginRequest, UserResponse>("api/users/login", request);
        }
    }
}
