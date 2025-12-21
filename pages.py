from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    Base page class that all page objects inherit from.
    """
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def find_element(self, locator):
        """Find element with explicit wait."""
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def click_element(self, locator):
        """Click element with explicit wait."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def enter_text(self, locator, text):
        """Enter text into element."""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        """Get text from element."""
        return self.find_element(locator).text
    
    def is_element_visible(self, locator):
        """Check if element is visible."""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False


class LoginPage(BasePage):
    """
    Page Object for Login Page.
    """
    
    # Locators
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.example.com/login"
    
    def navigate(self):
        """Navigate to login page."""
        self.driver.get(self.url)
        return self
    
    def login(self, username, password):
        """Perform login action."""
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)
        return HomePage(self.driver)
    
    def get_error_message(self):
        """Get error message text."""
        return self.get_text(self.ERROR_MESSAGE)
    
    def is_error_displayed(self):
        """Check if error message is displayed."""
        return self.is_element_visible(self.ERROR_MESSAGE)


class HomePage(BasePage):
    """
    Page Object for Home Page.
    """
    
    # Locators
    WELCOME_MESSAGE = (By.CLASS_NAME, "welcome-message")
    LOGOUT_BUTTON = (By.ID, "logout")
    USER_MENU = (By.CLASS_NAME, "user-menu")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.example.com/home"
    
    def is_logged_in(self):
        """Check if user is logged in."""
        return self.is_element_visible(self.WELCOME_MESSAGE)
    
    def get_welcome_message(self):
        """Get welcome message text."""
        return self.get_text(self.WELCOME_MESSAGE)
    
    def logout(self):
        """Perform logout action."""
        self.click_element(self.LOGOUT_BUTTON)
        return LoginPage(self.driver)


class SearchPage(BasePage):
    """
    Page Object for Search Page.
    """

    # Locators
    SEARCH_INPUT = (By.NAME, "q")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.search-btn")
    SEARCH_RESULTS = (By.CLASS_NAME, "search-results")
    RESULT_ITEMS = (By.CSS_SELECTOR, ".search-results .result-item")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.example.com/search"

    def navigate(self):
        """Navigate to search page."""
        self.driver.get(self.url)
        return self

    def search(self, query):
        """Perform search."""
        self.enter_text(self.SEARCH_INPUT, query)
        self.click_element(self.SEARCH_BUTTON)

    def get_results_count(self):
        """Get number of search results."""
        results = self.driver.find_elements(*self.RESULT_ITEMS)
        return len(results)

    def get_first_result_text(self):
        """Get text of first result."""
        first_result = self.wait.until(
            EC.presence_of_element_located(self.RESULT_ITEMS)
        )
        return first_result.text


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

    def click_login(self):
        """Click login button to open login page."""
        self.click_element(self.LOGIN_BUTTON)
        return WstyleLoginPage(self.driver)

    def click_logout(self):
        """Click logout button."""
        self.click_element(self.LOGOUT_BUTTON)
        return self

    def is_login_button_present(self):
        """Check if login button is present."""
        try:
            elements = self.driver.find_elements(*self.LOGIN_BUTTON)
            return len(elements) > 0
        except:
            return False

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


class WstyleLoginPage(BasePage):
    """
    Page Object for Wstyle.com.tw Login Page.
    """

    # Locators
    LOGIN_TITLE = (By.ID, "tbLoginHeader")
    USERNAME_LABEL = (By.ID, "ctl00_ContentPlaceHolder1_uc_login_lblUserName")
    PASSWORD_LABEL = (By.CSS_SELECTOR, "tr:nth-child(3) > td:nth-child(1)")
    USERNAME_INPUT = (By.ID, "ctl00_ContentPlaceHolder1_uc_login_edtUserid")
    PASSWORD_INPUT = (By.ID, "ctl00_ContentPlaceHolder1_uc_login_edtPwd")
    LOGIN_SUBMIT_BUTTON = (By.ID, "ctl00_ContentPlaceHolder1_uc_login_btnLogin")

    def get_login_title_text(self):
        """Get login title text."""
        return self.get_text(self.LOGIN_TITLE)

    def get_username_label_text(self):
        """Get username label text."""
        return self.get_text(self.USERNAME_LABEL)

    def get_password_label_text(self):
        """Get password label text."""
        return self.get_text(self.PASSWORD_LABEL)

    def login(self, username, password):
        """Perform login action."""
        self.click_element(self.USERNAME_INPUT)
        self.enter_text(self.USERNAME_INPUT, username)
        self.click_element(self.PASSWORD_INPUT)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_SUBMIT_BUTTON)
        return WstyleHomePage(self.driver)
