from pages.base_page import BasePage
from locators.cart_locators import CartLocators
from objects.product import Product

class CartPage(BasePage):
  def __init__(self, driver):
    super().__init__(driver)

  def get_cart_products(self):
    return self.get_elements_size(CartLocators.CART_ITEM)

  def remove_from_cart(self,index):
    self.click(CartLocators.LABEL_BUTTON_REMOVE(index))

  def get_cart_amount_badge(self):
    total = 0
    try:
      total = self.get_text(CartLocators.CART_AMOUNT)
    except Exception as identifier:
      print('err at',str(identifier))
    return int(total)

