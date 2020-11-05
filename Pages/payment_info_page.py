from Pages.base_page import BasePage
from Locators.payment_info_locators import PaymentInfoLocators

class PaymentInfoPage(BasePage):
  def get_header_title(self):
    return self.get_text(PaymentInfoLocators.HEADER_TITLE)

  def input_payment_info(self, paymentInfo):
    self.enter_text(PaymentInfoLocators.TEXTBOX_FIRSTNAME,paymentInfo.firstname)
    self.enter_text(PaymentInfoLocators.TEXTBOX_LASTNAME, paymentInfo.lastname)
    self.enter_text(PaymentInfoLocators.TEXTBOX_ZIPCODE, paymentInfo.zipcode)

  def click_continue_checkout(self):
    self.click(PaymentInfoLocators.BUTTON_CONTINUE)
