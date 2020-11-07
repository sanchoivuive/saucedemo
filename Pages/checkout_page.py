from Locators.checkout_locators import CheckoutLocators
from Objects.product import Product
from Pages.base_page import BasePage
from Utils.utilities import Utilities


class CheckoutPage(BasePage):
  def __init__(self, driver):
    super().__init__(driver)

  def get_product_info(self, index):
    name = self.get_text(CheckoutLocators.LABEL_PRODUCT_NAME(index))
    desc = self.get_text(CheckoutLocators.LABEL_PRODUCT_DESC(index))
    price = self.get_text(CheckoutLocators.LABEL_PRODUCT_PRICE(index))
    return Product(name, desc, price)

  def click_cancel_button(self):
    self.click(CheckoutLocators.BUTTON_CANCEL)

  def click_finish_button(self):
    self.click(CheckoutLocators.BUTTON_FINISH)

  # def calculate_total_price(self):

  def get_item_price(self):
    item_total = Utilities.get_number(self.get_text(CheckoutLocators.LABEL_ITEM_TOTAL))
    return float(item_total)

  def get_tax(self):
    tax = Utilities.get_number(self.get_text(CheckoutLocators.LABEL_TAX))
    return float(tax)

  def get_total(self):
    total = Utilities.get_number(self.get_text(CheckoutLocators.LABEL_TOTAL))
    return float(total)

  def calculate_the_price(item_price, tax, total):
    correct = False
    tax_rate = 0.08
    calculated_tax = round(item_price * tax_rate, 2)
    if (tax == calculated_tax) and (total == calculated_tax + item_price):
      correct = True
    return correct
