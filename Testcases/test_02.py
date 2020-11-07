import random
import time
import unittest

from Objects.account import Account
from Objects.payment_info import PaymentInfo
from Pages.cart_page import CartPage
from Pages.checkout_page import CheckoutPage
from Pages.finish_page import FinishPage
from Pages.login_page import LoginPage
from Pages.payment_info_page import PaymentInfoPage
from Pages.product_list_page import ProductListPage
from Testcases.base_test import BaseTest
from Testdata.data import StandardUser, PageData, PaymentInfoData
from Testdata.test_data import TestData
from Utils.assertion import Assertion
from Utils.utilities import Utilities


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

  def add_products_to_cart_randomly(self):
    # choose product randomly add to cart
    total_chosen_products = random.randint(1, 6)
    order_chosen_products = []
    for index_product in range(total_chosen_products):
      index_product = random.choice([i for i in range(1, 7) if i not in order_chosen_products])
      order_chosen_products.append(index_product)

    return order_chosen_products

  def test_checkout_cart(self):
    product_page = ProductListPage(self.driver)
    products = TestData.getProducts(self)
    list_selected_product = Test02.add_products_to_cart_randomly(self)
    print('list sp chon la', list_selected_product)
    for index in list_selected_product:
      product_page.add_to_cart(index)
      actual_product = product_page.get_product_info(index)
      expected_product = products[index - 1]
      assertion = Assertion()
      assertion.compare_products(actual_product, expected_product)
    product_page.click_product_badge_icon()

    cart_page = CartPage(self.driver)
    cart_page.click_checkout_cart()
    payment_info_page = PaymentInfoPage(self.driver)
    payment_url = payment_info_page.get_url()
    self.assertEqual(PageData.PAYMENT_INFO_URL, payment_url)
    self.assertIn(PageData.PAGE_TITLE, payment_info_page.get_title())
    self.assertIn('Checkout: Your Information', payment_info_page.get_header_title())

    payment_info = PaymentInfo(PaymentInfoData.FIRSTNAME, PaymentInfoData.LASTNAME, PaymentInfoData.ZIPCODE)
    payment_info_page.input_payment_info(payment_info)
    payment_info_page.click_continue_checkout()

    # compare subtotal, total, tax
    checkout_page = CheckoutPage(self.driver)
    expected_subtotal = 0
    for index in range(len(list_selected_product)):
      product_checkout = checkout_page.get_product_info(index + 1)
      product_checkout.price = Utilities.get_number(product_checkout.price)
      expected_subtotal += product_checkout.price
    actual_subtotal = checkout_page.get_item_price()
    self.assertEqual(expected_subtotal, actual_subtotal)
    expected_tax = Utilities.calculate_tax(expected_subtotal)
    actual_tax = checkout_page.get_tax()
    self.assertEqual(expected_tax, actual_tax)
    expected_total = Utilities.calculate_total(expected_subtotal, expected_tax)
    actual_total = checkout_page.get_total()
    self.assertEqual(expected_total, actual_total)

    checkout_page.click_finish_button()
    finish_page = FinishPage(self.driver)
    self.assertIn('Finish', finish_page.get_header_title())
    self.assertIn('THANK YOU FOR YOUR ORDER', finish_page.get_complete_title())
    self.assertIn('Your order has been dispatched, and will arrive just as fast as the pony can get there',
                  finish_page.get_complete_message())
    pony_img = finish_page.is_img_visible()
    self.assertTrue(pony_img)


if __name__ == '__main__':
  unittest.main()
