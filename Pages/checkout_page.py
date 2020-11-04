
from pages.base_page import BasePage
from locators.payment_info_locators import PaymentInfoLocators
from objects.product import Product
from utils.string_to_number import StringToNumber
class CheckoutPage(BasePage):
  def __init__(self, driver):
    super().__init__(driver)

  def get_product_info(self,index):
    name = self.get_text(PaymentInfoLocators.LABEL_PRODUCT_NAME(index))
    desc = self.get_text(PaymentInfoLocators.LABEL_PRODUCT_DESC(index))
    price = self.get_text(PaymentInfoLocators.LABEL_PRODUCT_PRICE(index))
    return Product(name,desc,price)

  def click_cancel_button(self):
    self.click(PaymentInfoLocators.BUTTON_CANCEL)

  def click_finish_button(self):
    self.click(PaymentInfoLocators.BUTTON_FINISH)

  # def calculate_total_price(self):

  def get_item_price(self):
    item_total = StringToNumber.get_number(self.get_text(PaymentInfoLocators.LABEL_ITEM_TOTAL))
    return item_total

  def get_tax(self):
    tax = StringToNumber.get_number(self.get_text(PaymentInfoLocators.LABEL_TAX))
    return tax

  def get_total(self):
    total = StringToNumber.get_number(self.get_text(PaymentInfoLocators.LABEL_TOTAL))
    return total