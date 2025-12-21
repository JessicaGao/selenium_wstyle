from selenium.webdriver.common.by import By
from pages import BasePage

class WstyleHomePage(BasePage):
    """
    Page Object for Wstyle.com.tw Home Page.
    """

    # Locators
    POPUP = (By.CLASS_NAME, "jumpdv")
    CLOSE_POPUP_BUTTON = (By.CLASS_NAME, "closeJ")
    LOGIN_BUTTON = (By.NAME, "login")
    LOGOUT_BUTTON = (By.NAME, "logout")
    MEMBER_BUTTON = (By.NAME, "imgMember")
    ORDER_BUTTON = (By.NAME, "imgOrder")
    CART_BUTTON = (By.NAME, "imgCart")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.wstyle.com.tw/Shop/"

    def navigate(self):
        """Navigate to wstyle home page."""
        self.driver.get(self.url)
        return self

    def is_popup_visible(self):
        """Check if popup is visible."""
        try:
            popup = self.driver.find_element(*self.POPUP)
            return popup.is_displayed()
        except:
            return False

    def close_popup(self):
        """Close popup if visible."""
        if self.is_popup_visible():
            self.click_element(self.CLOSE_POPUP_BUTTON)
        return self

    def is_login_button_present(self):
        """Check if login button is present."""
        try:
            elements = self.driver.find_elements(*self.LOGIN_BUTTON)
            return len(elements) > 0
        except:
            return False
    def click_login(self):
        """Click login button to open login page."""
        self.click_element(self.LOGIN_BUTTON)
        # return WstyleLoginPage(self.driver)

    def is_logout_button_present(self):
        """Check if logout button is present."""
        try:
            elements = self.driver.find_elements(*self.LOGOUT_BUTTON)
            return len(elements) > 0
        except:
            return False
    def click_logout(self):
        """Click logout button to open login page."""
        self.click_element(self.LOGOUT_BUTTON)
        # return WstyleLoginPage(self.driver)
    def is_member_button_present(self):
        """Check if member button is present."""
        try:
            elements = self.driver.find_elements(*self.MEMBER_BUTTON)
            return len(elements) > 0
        except:
            return False

    def is_order_button_present(self):
        """Check if order button is present."""
        try:
            elements = self.driver.find_elements(*self.ORDER_BUTTON)
            return len(elements) > 0
        except:
            return False

    def is_cart_button_present(self):
        """Check if cart button is present."""
        try:
            elements = self.driver.find_elements(*self.CART_BUTTON)
            return len(elements) > 0
        except:
            return False
    