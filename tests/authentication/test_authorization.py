import pytest

from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.authorization
class TestAuthorization:
    def test_successful_authorization(self, login_page: LoginPage, dashboard_page: DashboardPage,
                                      registration_page: RegistrationPage):
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.registration_form.fill(email='ovkochetova1@gmail.com', username='ovkochetova1', password='123qwe')
        registration_page.registration_form.click_registration_button()

        dashboard_page.dashboard_toolbar_view.check_visible()
        dashboard_page.navbar.check_visible('ovkochetova1')
        dashboard_page.sidebar.check_visible()
        dashboard_page.sidebar.click_logout()

        login_page.login_form.fill(email='ovkochetova1@gmail.com', password='123qwe')
        login_page.login_form.click_login_button()

        dashboard_page.dashboard_toolbar_view.check_visible()
        dashboard_page.navbar.check_visible('ovkochetova1')
        dashboard_page.sidebar.check_visible()

    @pytest.mark.parametrize('email,password', [
        ('ovkochetova1@gmail.com', '123qwe'),
        ('user.name@gmail.com', '  '),
        ('  ', 'password'), ])
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.login_form.fill(email=email, password=password)
        login_page.login_form.click_login_button()
        login_page.check_visible_wrong_email_or_password_alert()
        

    def test_navigate_from_authorization_to_registration(
            self,
            login_page: LoginPage,
            registration_page: RegistrationPage
    ):
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.click_registration_link()

        registration_page.registration_form.check_visible(email="", username="", password="")
