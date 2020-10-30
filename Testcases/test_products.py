# system, driver modules
import os
import sys
sys.path.append('.')
import time
import unittest

# import other modules
from testcases.base_test import BaseTest
from pages.product_list_page import ProductListPage
from testdata.data import PageData
from utils.json_services import JsonServices
from objects.product import Product

#get the directory path to output report file
dir = os.getcwd()

class TestProducts(BaseTest):

  @classmethod
  def setUp(self):
    super().setUp()

  @unittest.skip("no reason for skipping")
  def test_list_products(self):
    product_list_page = ProductListPage(self.driver)
    product_list_page.navigate_url(PageData.PRODUCT_LIST_URL)
    actual_products = []

    #get list actual products
    no_of_products = product_list_page.get_list_products()
    for i in range(1, no_of_products + 1):
      product = product_list_page.get_product_info(i)
      actual_products.append(product)

    # get list expected products
    path = ('..\\testdata\\listProducts.json')
    expected_products = JsonServices.json_to_list_object(path,'products','Product')

    # parse to object Product type
    new_list = []
    for i in range(len(expected_products)):
      product = Product(expected_products[i].name,expected_products[i].desc,expected_products[i].price)
      new_list.append(product)
    expected_products = new_list

    #compare 2 lists
    is_lists_identical = product_list_page.compare_list_products(expected_products,actual_products)
    self.assertTrue(is_lists_identical)

  def test_add_remove_product(self):
    product_list_page = ProductListPage(self.driver)
    product_list_page.navigate_url(PageData.PRODUCT_LIST_URL)
    actual_products = []

    # get list actual products
    no_of_products = product_list_page.get_list_products()

    for i in range(1, no_of_products + 1):
      self.assertTrue('ADD TO CART', product_list_page.check_button_add_exist(i))
      product_list_page.add_to_cart(i)
      self.assertTrue('REMOVE', product_list_page.check_button_remove_exist(i))
      amount_in_cart = product_list_page.get_product_badge()
      self.assertEqual(1, amount_in_cart)
      product_list_page.remove_from_cart(i)
      self.assertTrue('ADD TO CART', product_list_page.check_button_add_exist(i))

  @classmethod
  def tearDown(self):
    super().tearDown()

if __name__ == '__main__':
  unittest.main()