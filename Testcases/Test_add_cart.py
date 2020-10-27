# system, driver modules
import sys
sys.path.append('.')
import time
import unittest

from Testcases.BaseTest import BaseTest
from Pages.BasePage import BasePage
from Pages.ProductListPage import ProductListPage

class AddCart(BaseTest):
  @classmethod
  def setUp(self):
    super().setUp()
    print('hi Tien')

  def test_add_to_cart(self):
    product_list_page = ProductListPage(self.driver)
    product_list_page.navigate_url('https://www.saucedemo.com/inventory.html')

  @classmethod
  def tearDown(self):
    super().tearDown()

if __name__ == '__main__':
  unittest.main()

