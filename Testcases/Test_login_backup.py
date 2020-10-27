# system, driver modules
import sys
sys.path.append('.')
import time
import unittest

# import other modules
from Testcases.BaseTest import BaseTest
from Testdata.Data import StandardUser, PageData,PerformanceGlitchUser,ProblemUser,ItemInfo

from Pages.LoginPage import LoginPage
from Pages.ProductListPage import ProductListPage

from Objects.Account import Account
from Objects.Item import Item
from Locators.LoginPageLocators import LoginPageLocators
from Locators.ProductListPageLocators import ProductListPageLocators


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
    user = Account(ProblemUser.USERNAME, ProblemUser.PASSWORD)
    print('user la',user.username)
    login_page.login(user)

    # check the right title, url of result page
    product_page = ProductListPage(self.driver)
    self.assertIn('Swag Labs',product_page.get_title())
    loggedin_url = 'https://www.saucedemo.com/inventory.html'
    self.assertEqual(loggedin_url,product_page.get_url())
    #
    # #verify if 1st product is displayed
    # item = Item(ItemInfo.NAME,ItemInfo.DESC,ItemInfo.PRICE,ItemInfo.IMG_URL,ItemInfo.BUTTON_ADD,ItemInfo.BUTTON_REMOVE)
    #
    # product_name = result_page.get_product_name()
    # self.assertIn(item.name, product_name)
    #
    # product_desc = result_page.get_product_desc()
    # self.assertIn(item.desc,product_desc)
    #
    # product_price = result_page.get_product_price()
    # self.assertIn(item.price, product_price)
    #

    print('element size',product_page.get_broken_img())
    self.assertEqual(0, product_page.get_broken_img(),'\n actual: %i \n expected: 0' %(product_page.get_broken_img()))


    #verify the state of button
    # product_button_add = result_page.get_button_add()
    # self.assertIn(item.button_add, product_button_add, str(item.button_add) + 'not in %s' %(product_button_add))
    #
    # result_page.add_to_cart()
    # product_button_remove =result_page.get_button_remove()
    # self.assertIn(item.button_remove, product_button_remove, str(item.button_remove) + 'not in %s' % (product_button_remove))

    # product = Item(ItemInfo.NAME,ItemInfo.DESC,ItemInfo.PRICE,ItemInfo.IMG_URL,ItemInfo.BUTTON_ADD,ItemInfo.BUTTON_REMOVE)
    # product_expected = Item(ItemInfo.NAME,ItemInfo.DESC,ItemInfo.PRICE,ItemInfo.IMG_URL,ItemInfo.BUTTON_ADD,ItemInfo.BUTTON_REMOVE)
    # product_actual = result_page.get_product_info()
    # self.assertIn(product_expected.name,product_actual.name)
    # self.assertIn(product_expected.desc,product_actual.desc)
    # self.assertEqual(product_expected.img_url,product_actual.img_url)
    # self.assertIn(product_expected.button_add,product_actual.button_add)
    # self.assertIn(product_expected.button_remove,product_actual.button_remove)

  @classmethod
  def tearDown(self):
    super().tearDown()

if __name__ == '__main__':
  unittest.main()
