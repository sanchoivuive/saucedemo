from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from testdata.data import PageData

class LoginPage(BasePage):
  def __init__(self,driver):
    super().__init__(driver)
    self.navigate_url(PageData.BASE_URL)
    self.get_title()

  def login(self, user):
    self.enter_text(LoginLocators.INPUT_USERNAME, user.username)
    self.enter_text(LoginLocators.INPUT_PASSWORD, user.password)
    self.click(LoginLocators.BUTTON_LOGIN)

  def enter_username(self,username):
    self.enter_text(LoginLocators.INPUT_USERNAME, username)

  def enter_password(self,password):
    self.enter_text(LoginLocators.INPUT_PASSWORD, password)

  def click_button_login(self):
    self.click(LoginLocators.BUTTON_LOGIN)

  def get_message(self):
    return self.get_text(LoginLocators.LABEL_MESSAGE)
