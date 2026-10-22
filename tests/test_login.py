from pages.login_page import LoginPage

class TestLogin:

    def test_successful_login(self, driver):
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("standard_user", "secret_sauce")

        assert "inventory.html" in login_page.get_current_url()
        assert login_page.is_inventory_displayed()

    def test_locked_out_user(self, driver):
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("locked_out_user", "secret_sauce")

        error_text = login_page.get_error_message()
        assert "Epic sadface: Sorry, this user has been locked out." in error_text

    def test_invalid_credentials(self, driver):
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("standard_user", "wrong_password")

        error_text = login_page.get_error_message()
        assert "Username and password do not match" in error_text