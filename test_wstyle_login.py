import pytest
from home_page import WstyleHomePage
from login_page import  WstyleLoginPage    


class TestWstyleLogin:
    """
    Test login functionality for Wstyle.com.tw using Page Object Model.
    """

    @pytest.mark.ui
    def test_successful_login_and_logout(self, browser_driver):
        """Test complete login flow with element verification and logout."""
        # Navigate to home page and handle popup
        home_page = WstyleHomePage(browser_driver)
        login_page = WstyleLoginPage(browser_driver)
        home_page.navigate().close_popup()

        # Set window size
        browser_driver.set_window_size(999, 889)

        # Verify login button is present
        assert home_page.is_login_button_present()

        # Click login button to navigate to login page
        home_page.click_login()

        # Verify login form elements
        assert login_page.get_login_title_text() in ["[Login]", "[登入]"]
        assert login_page.get_username_label_text() in ["Account", "帳號"]
        assert login_page.get_password_label_text() in ["Password", "密碼 :"]

        # Perform login
        login_page.login("hamburger", "hamburger")

        # Verify logout button is still present (logged in state)
        assert home_page.is_logout_button_present()

        # Logout
        home_page.click_logout()

        # Verify login button is still present after logout
        assert home_page.is_login_button_present()


class TestWstyleHomePage:
    """
    Test navigation elements for Wstyle.com.tw using Page Object Model.
    """

    @pytest.mark.ui
    def test_navigation_elements_present(self, browser_driver):
        """Verify all main navigation elements are present on the page."""
        # Navigate to home page
        home_page = WstyleHomePage(browser_driver)
        home_page.navigate()

        # Set window size
        browser_driver.set_window_size(999, 889)

        # Verify all navigation elements are present
        assert home_page.is_login_button_present(), "Login button should be present"
        assert home_page.is_member_button_present(), "Member button should be present"
        assert home_page.is_order_button_present(), "Order button should be present"
        assert home_page.is_cart_button_present(), "Cart button should be present"
