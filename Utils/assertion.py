import unittest

class Assertion(unittest.TestCase):
  def compare_products(self, actual_product, expected_product):
    try:
      self.assertEqual(actual_product.name, expected_product.name)
    except AssertionError:
      print('Actual product name is: %s \n   VS \nExpected product name is: %s ' %(actual_product.name,
                                                                                  expected_product.name))
    try:
      self.assertEqual(actual_product.desc, expected_product.desc)
    except AssertionError:
      print('Actual product description is: %s \n   VS \nExpected product description is: %s ' %(actual_product.desc,
                                                                                                expected_product.desc))
    try:
      self.assertEqual(actual_product.price, expected_product.price)
    except AssertionError:
      print('Actual product price is: %s \n   VS \nExpected product price is: %s ' %(actual_product.price,
                                                                                    expected_product.price))