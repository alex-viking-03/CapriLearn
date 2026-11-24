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
using CapriFrontendNew.Services;
using CapriFrontendNew.Views.Authentication;

namespace CapriFrontendNew
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            ShowLogin();
        }

        private void ShowLogin()
        {
            var loginView = new LoginView(new ApiClient());

            loginView.RegisterRequired += (sender, args) =>
            {
                ShowRegister();
            };

            AuthContent.Content = loginView;
        }

        private void ShowRegister()
        {
            var registerView = new RegisterView();

            registerView.LoginRequired += (sender, args) =>
            {
                ShowLogin();
            };

            AuthContent.Content = registerView;
        }
    }
}