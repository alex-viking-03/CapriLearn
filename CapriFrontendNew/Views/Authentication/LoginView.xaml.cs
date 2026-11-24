using CapriFrontendNew.Models.Authentication;
using CapriFrontendNew.Services;
using System.Net.Http;
using System.Windows;
using System.Windows.Controls;

namespace CapriFrontendNew.Views.Authentication
{
    public partial class LoginView : UserControl
    {
        private readonly ApiClient _apiClient;
        public event EventHandler RegisterRequired;

        private void RegisterButton_Click(object sender, RoutedEventArgs e)
        {
            RegisterRequired?.Invoke(this, EventArgs.Empty);
        }

        public LoginView(ApiClient apiClient)
        {
            InitializeComponent();
            _apiClient = apiClient;
        }

        public async void EnterButton_Click(object sender, RoutedEventArgs e)
        {
            LoginRequest request = new LoginRequest
            {
                Email = EmailTB.Text,
                Password = PasswordPB.Password
            };

            try
            {
                var user = await _apiClient.PostAsync<LoginRequest, UserResponse>("api/users/login", request);

                if(user != null)
                {
                    MessageBox.Show($"Добро пожаловать {user.Username}!");
                }
            }
            catch(HttpRequestException ex)
            {
                MessageBox.Show($"Ошибка входа: {ex.Message}");
            }
            catch(Exception ex)
            {
                MessageBox.Show($"Error: {ex.Message}");
            }
        }
    }
}
