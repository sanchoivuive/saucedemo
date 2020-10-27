#system, driver modules
import sys
sys.path.append('.')
import time
import unittest

#import other modules
from Testcases.BaseTest import BaseTest
from Testdata.Data import PageData,StandardUser,InvalidLoginMessage,FakeUser
from Pages.LoginPage import LoginPage
from Pages.ProductListPage import ProductListPage
from Objects.Account import Account
from Locators.LoginPageLocators import LoginPageLocators
from Locators.ProductListPageLocators import ProductListPageLocators

class LoginInvalid(BaseTest):
  @classmethod
  def setUp(self):
    super().setUp()
    self.login_page = LoginPage(self.driver)
    # self.result_page = ProductListPage(self.driver)
    self.user = Account('','')
    # self.assertTrue(self.login_page.check_title(LoginData.PAGE_TITLE))
    print('hi Tien')

  def test_login_blank(self):
    # self.assertTrue(self.login_page.check_title(LoginData.PAGE_TITLE))
    access_result = self.login_page.verify_title(PageData.PAGE_TITLE)
    self.assertTrue(access_result)
    # print('da confirm co title',access_result)
    self.login_page.click_button_login()
    login_result = self.login_page.get_message()
    self.assertIn(InvalidLoginMessage.USERNAME_REQUIRED_MESSAGE,login_result)

  def test_login_blank_username(self):
    #verify successfully access login page
    self.assertTrue(self.login_page.verify_title(PageData.PAGE_TITLE))

    #Action log in here
    self.login_page.enter_password(StandardUser.PASSWORD)
    self.login_page.login(self.user)

    #verify log in unsuccessfuly
    login_result = self.login_page.get_message()
    print('mess la blank USERNAME là', self.login_page.get_message())
    self.assertIn(InvalidLoginMessage.USERNAME_REQUIRED_MESSAGE,login_result)

  def test_login_blank_password(self):
    # verify successfully access login page
    self.assertTrue(self.login_page.verify_title(PageData.PAGE_TITLE))

    # Action log in here
    self.login_page.enter_username(StandardUser.USERNAME)
    self.login_page.login(self.user)

    # verify log in unsuccessfuly
    login_result = self.login_page.get_message()
    self.assertIn(InvalidLoginMessage.PASSWORD_REQUIRED_MESSAGE,login_result)

  def test_login_invalid_user(self):
    # verify successfully access login page
    self.assertTrue(self.login_page.verify_title(PageData.PAGE_TITLE))

    # Action log in here
    self.login_page.enter_username(FakeUser.USERNAME)
    self.login_page.enter_password(FakeUser.PASSWORD)
    # self.assertTrue(self.login_page.check_title(LoginData.PAGE_TITLE))
    self.login_page.login(self.user)

    # verify log in unsuccessfuLly
    login_result = self.login_page.get_message()
    self.assertIn(InvalidLoginMessage.INVALID_USER_MESSAGE, login_result)

  '''def test_login_banned_user(self):
    self.user = Account(LoginData.BANNED_USER.get('username'), LoginData.BANNED_USER.get('password'))
    # self.assertTrue(self.login_page.check_title(LoginData.PAGE_TITLE))
    self.login_page.login(self.user)
    self.assertIn(LoginData.BANNED_USER_MESSAGE, self.result_page.get_message())

  def test_login_invalid_username(self):
    self.user = Account(LoginData.FAKE_USER.get('username'), LoginData.STANDARD_USER.get('password'))
    # self.assertTrue(self.login_page.check_title(LoginData.PAGE_TITLE))
    self.login_page.login(self.user)
    self.assertIn(LoginData.INVALID_USER_MESSAGE, self.result_page.get_message())

  def test_login_invalid_password(self):
    self.user = Account(LoginData.STANDARD_USER.get('username'), LoginData.FAKE_USER.get('password'))
    self.login_page.login(self.user)
    self.assertIn(LoginData.INVALID_USER_MESSAGE, self.result_page.get_message())'''

  @classmethod
  def tearDown(self):
    super().tearDown()

if __name__ == '__main__':
  unittest.main()