from selenium.webdriver.common.by import By


class PaymentInfoLocators(object):
  HEADER_TITLE = (By.XPATH, '//*[@id="contents_wrapper"]//div[@class="subheader"]')

  TEXTBOX_FIRSTNAME = (By.XPATH, '//*[@id="first-name"]')
  TEXTBOX_LASTNAME = (By.XPATH, '//*[@id="last-name"]')
  TEXTBOX_ZIPCODE = (By.XPATH, '//*[@id="postal-code"]')

  BUTTON_CONTINUE = (By.XPATH, '//div[@class="checkout_buttons"]/input')
  BUTTON_CANCEL = (By.XPATH, '//div[@class="checkout_buttons"]/a')
