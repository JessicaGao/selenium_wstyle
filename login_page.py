from selenium.webdriver.common.by import By
from pages import BasePage

class WstyleLoginPage(BasePage):
    """
    Page Object for Wstyle.com.tw Login Page.
    """

    # Locators
    LOGIN_TITLE = (By.ID, "tbLoginHeader")
    LOGOUT_BUTTON = (By.NAME, "logout")
    USERNAME_LABEL = (By.ID, "ctl00_ContentPlaceHolder1_uc_login_lblUserName")
    PASSWORD_LABEL = (By.CSS_SELECTOR, "tr:nth-child(3) > td:nth-child(1)")
    USERNAME_INPUT = (By.ID, "ctl00_ContentPlaceHolder1_uc_login_edtUserid")
    PASSWORD_INPUT = (By.ID, "ctl00_ContentPlaceHolder1_uc_login_edtPwd")
    LOGIN_SUBMIT_BUTTON = (By.ID, "ctl00_ContentPlaceHolder1_uc_login_btnLogin")


    def click_logout(self):
        """Click logout button."""
        self.click_element(self.LOGOUT_BUTTON)
        return self

    
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
        # return WstyleHomePage(self.driver)