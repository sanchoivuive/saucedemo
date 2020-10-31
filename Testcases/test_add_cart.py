import unittest
from testcases.base_test import BaseTest
from pages.product_list_page import ProductListPage
# from pages.cart_page import CartPage
class AddCart(BaseTest):

  @classmethod
  def setUp(self):
    super().setUp()

  @classmethod
  def tearDown(self):
    super().tearDown()

  def test_add_products_to_cart(self):
    product_list_page = ProductListPage(self.driver)
    cart_page = 0
    pass


if __name__ == '__main__':
  unittest.main()