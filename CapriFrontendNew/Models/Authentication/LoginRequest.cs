using System;
using System.Text.Json.Serialization;

namespace CapriFrontendNew.Models.Authentication
{
    public class LoginRequest
    {
        [JsonPropertyName("email")]
        public string Email { get; set; }

        [JsonPropertyName("password")]
        public string Password { get; set; }
    }
}
