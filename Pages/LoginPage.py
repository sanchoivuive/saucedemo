from Pages.BasePage import BasePage
from Locators.LoginPageLocators import LoginPageLocators
from Testdata.Data import PageData

class LoginPage(BasePage):
  def __init__(self,driver):
    super().__init__(driver)
    self.navigate_url(PageData.BASE_URL)
    self.get_title()

  def login(self, user):
    self.enter_text(LoginPageLocators.INPUT_USERNAME, user.username)
    self.enter_text(LoginPageLocators.INPUT_PASSWORD, user.password)
    self.click(LoginPageLocators.BUTTON_LOGIN)

  def enter_username(self,username):
    self.enter_text(LoginPageLocators.INPUT_USERNAME, username)

  def enter_password(self,password):
    self.enter_text(LoginPageLocators.INPUT_PASSWORD, password)

  def click_button_login(self):
    self.click(LoginPageLocators.BUTTON_LOGIN)