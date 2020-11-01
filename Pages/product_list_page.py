from pages.base_page import BasePage
from locators.product_list_locators import ProductListLocators
from objects.product import Product


class ProductListPage(BasePage):
  def __init__(self, driver):
    super().__init__(driver)

  def get_broken_img(self):
    return self.get_elements_size(ProductListLocators.BROKEN_IMAGE)

  def get_list_products(self):
    return self.get_elements_size(ProductListLocators.CART_ITEM1)

  def add_to_cart(self,index):
    self.click(ProductListLocators.LABEL_BUTTON_ADD(index))

  def remove_from_cart(self,index):
    self.click(ProductListLocators.LABEL_BUTTON_REMOVE(index))

  def check_button_add_exist(self,index):
    return self.get_text(ProductListLocators.LABEL_BUTTON_ADD(index))

  def check_button_remove_exist(self,index):
    return self.is_visible(ProductListLocators.LABEL_BUTTON_REMOVE(index))

  def get_product_badge(self):
    total = 0
    try:
      total = self.get_text(ProductListLocators.CART_AMOUNT)
    except Exception as identifier:
      print('err at',str(identifier))
    return int(total)

  def get_product_info(self,index):
    name = self.get_text(ProductListLocators.LABEL_PRODUCT_NAME(index))
    desc = self.get_text(ProductListLocators.LABEL_PRODUCT_DESC(index))
    price = self.get_text(ProductListLocators.LABEL_PRODUCT_PRICE(index))
    return Product(name,desc,price)

  def check_cart_exist(self):
    return self.is_visible(ProductListLocators.CART_ICON)

  def check_menu_hamburger_exist(self):
    return self.is_visible(ProductListLocators.MENU_HAMBURGER)

  def compare_list_products(self,expected,actual):
    lists_are_identical = False
    if len(expected) != len(actual):
      return lists_are_identical
    else:
      for i in range(len(expected)):
        (expected[i].name in actual[i].name) and (expected[i].desc in actual[i].desc) and (expected[i].price in actual[i]
         .price)
      lists_are_identical = True
      return lists_are_identical

  def is_product_badge_invisible(self):
    return self.is_invisible(ProductListLocators.CART_AMOUNT)

  def click_product_badge_icon(self):
    return self.click(ProductListLocators.CART_ICON)

