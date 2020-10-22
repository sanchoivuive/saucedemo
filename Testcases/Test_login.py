# system, driver modules
import sys
sys.path.append('.')
import time
import unittest

# import other modules
from Testcases.BaseTest import BaseTest
from Testdata.Data import StandardUser, PageData

from Pages.LoginPage import LoginPage
from Pages.ProductListPage import ProductListPage

from Objects.Account import Account
from Locators.LoginPageLocators import LoginPageLocators
from Locators.ProductListPageLocators import ProductListPageLocators


class Login(BaseTest):

  @classmethod
  def setUp(self):
    super().setUp()
    self.login_page = LoginPage(self.driver)
    self.result_page = ProductListPage(self.driver)
    print('hi Tien')

  def test_login_standard_user(self):
    # constructor
    # login_page = LoginPage(self.driver)
    # result_page = LoginResultPage(self.driver)
    user = Account(StandardUser.USERNAME,StandardUser.PASSWORD)

    # check the right title of login page
    self.login_page.verify_title(PageData.PAGE_TITLE)
    print('da check xong title')
    self.login_page.login(user)

    # check the right title of result page
    self.result_page.verify_title(PageData.PAGE_TITLE)
    # self.assertIn('Products', self.result_page.get_header_title())
    print('check xong title',self.result_page.verify_title(PageData.PAGE_TITLE))
    time.sleep(1)

  '''def test_login_glitch_user(self):
    user = Account(LoginData.GLITCH_USER.get('username'), LoginData.GLITCH_USER.get('password'))

    # check the right title of login page
    self.assertTrue(self.login_page.check_title(LoginData.PAGE_TITLE))
    self.login_page.login(user)

    # check the right title of result page
    self.assertTrue(self.result_page.check_title(LoginData.PAGE_TITLE))
    self.assertIn('Products', self.result_page.get_header_title())
    time.sleep(1)

  def test_login_problem_user(self):
    user = Account(LoginData.PROBLEM_USER.get('username'), LoginData.PROBLEM_USER.get('password'))

    # check the right title of login page
    self.assertTrue(self.login_page.check_title(LoginData.PAGE_TITLE))
    self.login_page.login(user)

    # check the right title of result page
    self.assertTrue(self.result_page.check_title(LoginData.PAGE_TITLE))
    self.assertIn('Products', self.result_page.get_header_title())
    time.sleep(1)'''

  @classmethod
  def tearDown(self):
    super().tearDown()


if __name__ == '__main__':
  unittest.main()
