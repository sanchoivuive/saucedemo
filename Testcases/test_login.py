# system, driver modules
import sys
sys.path.append('.')
import time
import unittest

# import other modules
from Testcases.base_test import BaseTest
from Testdata.data import StandardUser, PageData,PerformanceGlitchUser,ProblemUser,ItemInfo

from Pages.login_page import LoginPage
from Pages.product_list_page import ProductListPage

from Objects.account import Account
# from Objects.Item import Item
from Objects.product import Product
from Locators.login_locators import LoginLocators
from Locators.product_list_locators import ProductListLocators


class Login(BaseTest):

  @classmethod
  def setUp(self):
    super().setUp()
    print('hi Tien')

  def test_login_standard_user(self):
    # access & check the right title of login page
    login_page = LoginPage(self.driver)
    self.assertIn('Swag Labs',login_page.get_title())

    #Action login to page
    user = Account(StandardUser.USERNAME, StandardUser.PASSWORD)
    print('user dang login la',user.username)
    login_page.login(user)

    # check the right title, url after login successful
    product_list_page = ProductListPage(self.driver)
    self.assertIn('Swag Labs',product_list_page.get_title())
    self.assertEqual(PageData.PRODUCT_LIST_URL,product_list_page.get_url())

    #check the hamburger button exist
    self.assertTrue(product_list_page.check_cart_exist())

    #check the visible of cart
    self.assertTrue(product_list_page.check_menu_hamburger_exist())

  @classmethod
  def tearDown(self):
    super().tearDown()

if __name__ == '__main__':
  unittest.main()
