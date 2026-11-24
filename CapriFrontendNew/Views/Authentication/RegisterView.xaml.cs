using CapriFrontendNew.Models.Authentication;
using CapriFrontendNew.Services;
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace CapriFrontendNew.Views.Authentication
{
    public partial class RegisterView : UserControl
    {
        public readonly AuthenticationService _authService;
        public event EventHandler LoginRequired;

        public RegisterView()
        {
            InitializeComponent();

            var apiClient = new ApiClient();
            _authService = new AuthenticationService(apiClient);
        }

        private async void RegisterButton_Click(object sender, RoutedEventArgs e)
        {
            var request = new RegisterRequest
            {
                Email = EmailTB.Text,
                Username = UsernameTB.Text,
                Password = PasswordPB.Password
            };

            try
            {
                var user = await _authService.RegisterAsync(request);

                if(user != null)
                {
                    MessageBox.Show($"Аккаунт создан! Добро пожаловать {user.Username}");
                }
            }
            catch(HttpRequestException ex)
            {
                MessageBox.Show($"Ошибка регистрации: {ex.Message}");
            }
            catch(Exception ex)
            {
                MessageBox.Show($"Error: {ex.Message}");
            }
        }

        private void LoginButton_Click(object sender, RoutedEventArgs e)
        {
            LoginRequired?.Invoke(this, EventArgs.Empty);
        }

        
    }
}
