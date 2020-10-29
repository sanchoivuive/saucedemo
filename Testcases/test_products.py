# system, driver modules
import os
import sys
sys.path.append('.')
import time
import unittest
from collections import namedtuple
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

  def test_product_exist(self):
    product_list_page = ProductListPage(self.driver)
    product_list_page.navigate_url(PageData.PRODUCT_LIST_URL)
    actual_products = []
    expected_products = []

    for i in range(1, 7):
      product = product_list_page.get_product_info(i)
      self.assertTrue('ADD TO CART', product_list_page.check_button_add_exist(i))
      product_list_page.add_to_cart(i)
      self.assertTrue('REMOVE', product_list_page.check_button_remove_exist(i))
      amount_in_cart = product_list_page.get_product_badge()
      # print('so luong -->', amount_in_cart)
      self.assertEqual(1, amount_in_cart)
      product_list_page.remove_from_cart(i)
      self.assertTrue('ADD TO CART', product_list_page.check_button_add_exist(i))
      actual_products.append(product)

    print('actual', actual_products)
    print(type(actual_products))
    print('actual produc name',actual_products[1].name)
    print('actual produc quantity', actual_products[1].quantity)

    path = ('..\\testdata\\listProducts.json')
    expected_products = JsonServices.json_to_list_object(path,'products','Product')
    print('expected',expected_products)
    print(type(expected_products))
    print(type(expected_products[1]))

    newlist = []
    for i in range(len(expected_products)):
      a = Product(expected_products[i].name,expected_products[i].desc,expected_products[i].price)
      newlist.append(a)
    print('a',newlist)
    print('name',newlist[1].name)
    print('quantity', newlist[1].quantity)




  @classmethod
  def tearDown(self):
    super().tearDown()

if __name__ == '__main__':
  unittest.main()