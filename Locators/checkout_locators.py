from selenium.webdriver.common.by import By

class CheckoutLocators(object):
  CART_ITEM = '//*[@class="cart_list"]/div[@class="cart_item"]['
  PAYMENT_INFORMATION = (By.XPATH, '//div[@class="summary_info"]/div[@class="summary_value_label"][1]')
  SHIPPING_INFORMATION = (By.XPATH, '//div[@class="summary_info"]/div[@class="summary_value_label"][2]')

  LABEL_ITEM_TOTAL = (By.XPATH,'//div[@class="summary_info"]/div[@class="summary_subtotal_label"]')
  LABEL_TAX = (By.XPATH,'//div[@class="summary_info"]/div[@class="summary_tax_label"]')
  LABEL_TOTAL = (By.XPATH,'//div[@class="summary_info"]/div[@class="summary_total_label"]')

  BUTTON_CANCEL = (By.XPATH, '//div[@class="cart_footer"]/a[text()="CANCEL"]')
  BUTTON_FINISH = (By.XPATH, '//div[@class="cart_footer"]/a[text()="FINISH"]')

  def LABEL_PRODUCT_NAME(index):
    ITEM = ']//div[@class="inventory_item_name"]'
    return (By.XPATH, CheckoutLocators.CART_ITEM + str(index) + ITEM)

  def LABEL_PRODUCT_DESC(index):
    ITEM = ']//div[@class="inventory_item_desc"]'
    return (By.XPATH, CheckoutLocators.CART_ITEM + str(index) + ITEM)

  def LABEL_PRODUCT_PRICE(index):
    ITEM = ']//div[@class="inventory_item_price"]'
    return (By.XPATH, CheckoutLocators.CART_ITEM + str(index) + ITEM)

  def LABEL_PRODUCT_QUANTITY(index):
    ITEM = ']//div[@class="summary_quantity"]'
    return (By.XPATH, CheckoutLocators.CART_ITEM + str(index) + ITEM)
