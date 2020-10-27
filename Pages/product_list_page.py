from pages.base_page import BasePage
from locators.product_list_locators import ProductListLocators
from objects.product import Product



class ProductListPage(BasePage):
  def __init__(self, driver):
    super().__init__(driver)

  def get_broken_img(self):
    return self.get_elements_size(ProductListLocators.BROKEN_IMAGE)

  def add_to_cart_1(self,index):
    self.click(ProductListLocators.LABEL_BUTTON_ADD(index))

  def remove_from_cart_1(self,index):
    self.click(ProductListLocators.LABEL_BUTTON_REMOVE(index))

  def get_button_add(self):
    return self.get_text(ProductListLocators.ITEM_BUTTON_ADD)

  def add_to_cart(self):
    self.click(ProductListLocators.ITEM_BUTTON_ADD)

  def get_button_remove(self):
    return self.get_text(ProductListLocators.ITEM_BUTTON_REMOVE)

  def remove_from_cart(self):
    self.click(ProductListLocators.ITEM_BUTTON_REMOVE)

  def get_product_info(self,index):
    name = self.get_text(ProductListLocators.LABEL_PRODUCT_NAME(index))
    desc = self.get_text(ProductListLocators.LABEL_PRODUCT_DESC(index))
    price = self.get_text(ProductListLocators.LABEL_PRODUCT_PRICE(index))
    return Product(name,desc,price)
