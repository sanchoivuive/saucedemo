import unittest
from testcases.base_test import BaseTest
from pages.product_list_page import ProductListPage
from pages.cart_page import CartPage
from objects.account import Account
from pages.login_page import LoginPage
from pages.payment_info_page import PaymentInfoPage
from testdata.data import StandardUser,PageData,PaymentInfoData
from utils.assertion import Assertion
from testdata.test_data import TestData
from objects.payment_info import PaymentInfo
import random
import time

class Test02(BaseTest):

  @classmethod
  def setUp(self):
    super().setUp()
    login_page = LoginPage(self.driver)
    login_page.login(Account(StandardUser.USERNAME, StandardUser.PASSWORD))

  @classmethod
  def tearDown(self):
    super().tearDown()

  def cart_to_be_checkout(self):
    product_page = ProductListPage(self.driver)
    products = TestData.getProducts(self)
    for index in [1, 2, 3]:
      product_page.add_to_cart(index)
    product_page.click_product_badge_icon()

    cart_page = CartPage(self.driver)
    self.assertEqual(PageData.CART_URL, cart_page.get_url())
    list_get_product = []
    for index in [1, 2, 3]:
      actual_product = cart_page.get_product_info(index)
      list_get_product.append(actual_product)
      expected_product = products[index - 1]
      assertion = Assertion()
      assertion.compare_products(actual_product, expected_product)

    return list_get_product

  @unittest.skip("no reason for skipping")
  def test_products_in_cart(self):
    product_page = ProductListPage(self.driver)
    products = TestData.getProducts(self)
    for index in [1, 2, 3]:
      product_page.add_to_cart(index)
      time.sleep(1)
    product_page.click_product_badge_icon()


    cart_page = CartPage(self.driver)
    for index in [1, 2, 3]:
      actual_product = cart_page.get_product_info(index)
      expected_product = products[index - 1]
      assertion = Assertion()
      assertion.compare_products(actual_product, expected_product)

  @unittest.skip("no reason for skipping")
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
      time.sleep(1)

    #add chosen products to cart & compare products
    product_page.click_product_badge_icon()
    cart_page = CartPage(self.driver)

    for index in range (total_chosen_products):
      actual_product = cart_page.get_product_info(index + 1)
      expected_product = products[(order_chosen_products[index])]
      assertion = Assertion()
      assertion.compare_products(actual_product, expected_product)

  @unittest.skip("no reason for skipping")
  def test_continue_shopping(self):
    cart_page = CartPage(self.driver)
    aaa = Test02.cart_to_be_checkout(self)
    cart_page.click_continue_shopping()
    product_page = ProductListPage(self.driver)
    # product_page

  def test_checkout_cart(self):
    cart_page = CartPage(self.driver)
    list_selected_product = Test02.cart_to_be_checkout(self)
    cart_page.click_checkout_cart()
    payment_info_page = PaymentInfoPage(self.driver)
    payment_url = payment_info_page.get_url()
    self.assertEqual(PageData.PAYMENT_INFO_URL, payment_url)
    self.assertIn(PageData.PAGE_TITLE, payment_info_page.get_title())
    self.assertIn('Checkout: Your Information',payment_info_page.get_header_title())

    payment_info = PaymentInfo(PaymentInfoData.FIRSTNAME, PaymentInfoData.LASTNAME, PaymentInfoData.ZIPCODE)
    payment_info_page.input_payment_info(payment_info)
    payment_info_page.click_continue_checkout()



if __name__ == '__main__':
  unittest.main()