# system, driver modules
import sys
sys.path.append('.')
import time
import unittest

# import other modules
from testcases.base_test import BaseTest
from testdata.data import StandardUser, PageData,PerformanceGlitchUser,ProblemUser,ItemInfo

from pages.login_page import LoginPage
from pages.product_list_page import ProductListPage

from objects.account import Account
# from Objects.Item import Item
from objects.product import Product
from locators.login_locators import LoginLocators
from locators.product_list_locators import ProductListLocators


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
    print('user la',user.username)
    login_page.login(user)

    # check the right title, url of result page
    product_page = ProductListPage(self.driver)
    self.assertIn('Swag Labs',product_page.get_title())
    loggedin_url = 'https://www.saucedemo.com/inventory.html'
    self.assertEqual(loggedin_url,product_page.get_url())

    # print('element size',product_page.get_broken_img())
    # self.assertEqual(0, product_page.get_broken_img(),'\n actual: %i \n expected: 0' %(product_page.get_broken_img()))
    list_products = []
    for i in range (1,7):
      product = product_page.get_product_info(i)
      list_products.append(product.__str__())
    print(list_products)

  @classmethod
  def tearDown(self):
    super().tearDown()

if __name__ == '__main__':
  unittest.main()
