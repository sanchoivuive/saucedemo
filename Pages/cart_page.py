from pages.base_page import BasePage
from locators.cart_locators import CartLocators
from objects.product import Product

class CartPage(BasePage):
  def __init__(self, driver):
    super().__init__(driver)

  def get_product_info(self,index):
    name = self.get_text(CartLocators.LABEL_PRODUCT_NAME(index))
    desc = self.get_text(CartLocators.LABEL_PRODUCT_DESC(index))
    price = self.get_text(CartLocators.LABEL_PRODUCT_PRICE(index))
    quantity = self.get_text(CartLocators.LABEL_PRODUCT_QUANTITY(index))
    return Product(name, desc, price, quantity)

  def remove_from_cart(self, index):
    self.click(CartLocators.LABEL_BUTTON_REMOVE(index))

  def click_checkout_cart(self):
    self.click(CartLocators.BUTTON_CHECKOUT)

  def click_continue_shopping(self):
    self.click(CartLocators.BUTTON_CONTINUE_SHOPPING)
