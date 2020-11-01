import unittest
from testcases.base_test import BaseTest
from pages.product_list_page import ProductListPage
from pages.cart_page import CartPage
from objects.account import Account
from pages.login_page import LoginPage
from testdata.data import StandardUser
from utils.assertion import Assertion
from testdata.test_data import TestData
import random

class TestCartPage(BaseTest):

  @classmethod
  def setUp(self):
    super().setUp()
    login_page = LoginPage(self.driver)
    login_page.login(Account(StandardUser.USERNAME, StandardUser.PASSWORD))

  @classmethod
  def tearDown(self):
    super().tearDown()

  @unittest.skip("no reason for skipping")
  def test_products_in_cart(self):
    product_page = ProductListPage(self.driver)
    products = TestData.getProducts(self)
    for index in [1, 2, 3]:
      product_page.add_to_cart(index)
    product_page.click_product_badge_icon()

    cart_page = CartPage(self.driver)
    for index in [1, 2, 3]:
      actual_product = cart_page.get_product_info(index)
      expected_product = products[index - 1]
      assertion = Assertion()
      assertion.compare_products(actual_product, expected_product)

  def test_products_in_cart2(self):
    product_page = ProductListPage(self.driver)
    products = TestData.getProducts(self)

    #choose product randomly add to cart
    total_chosen_products = random.randint(1,6)
    print('total sp la',total_chosen_products)
    order_chosen_products = []
    for index_product in range (total_chosen_products):
      index_product = random.choice([i for i in range(0,6) if i not in order_chosen_products])
      order_chosen_products.append(index_product)
      product_page.add_to_cart(index_product + 1)

    #add chosen products to cart & compare products
    product_page.click_product_badge_icon()
    cart_page = CartPage(self.driver)

    for index in range (len(order_chosen_products)):
      actual_product = cart_page.get_product_info(index + 1)
      expected_product = products[(order_chosen_products[index])]
      assertion = Assertion()
      assertion.compare_products(actual_product, expected_product)

  

if __name__ == '__main__':
  unittest.main()