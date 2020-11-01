from selenium.webdriver.common.by import By

class CartLocators(object):
  # HEADER_TITLE = (By.XPATH, '//*[@id="contents_wrapper"]/div[@class="subheader"]')
  CART_ITEM = '//div[@class="cart_list"]//div[@class="cart_item"]['
  # CART_ICON = (By.XPATH, '//*[@id="shopping_cart_container"]')
  CART_AMOUNT = (By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
  BUTTON_CONTINUE_SHOPPING = (By.XPATH,'//div[@class="cart_footer"]/a[text()="Continue Shopping"]')
  BUTTON_CHECKOUT = (By.XPATH, '//div[@class="cart_footer"]/a[text()="CHECKOUT"]')

  def LABEL_PRODUCT_NAME(index):
    ITEM = ']//div[@class="inventory_item_name"]'
    return (By.XPATH, CartLocators.CART_ITEM + str(index) + ITEM)

  def LABEL_PRODUCT_DESC(index):
    ITEM = ']//div[@class="inventory_item_desc"]'
    return (By.XPATH, CartLocators.CART_ITEM + str(index) + ITEM)

  def LABEL_PRODUCT_PRICE(index):
    ITEM = ']//div[@class="inventory_item_price"]'
    return (By.XPATH, CartLocators.CART_ITEM + str(index) + ITEM)

  def LABEL_PRODUCT_QUANTITY(index):
    ITEM = ']//div[@class="cart_quantity"]'
    return (By.XPATH, CartLocators.CART_ITEM + str(index) + ITEM)

  def BUTTON_REMOVE_PRODUCT(index):
    ITEM = ']//button[contains(@class, "btn_secondary") and contains(@class, "cart_button")]'
    return (By.XPATH, CartLocators.CART_ITEM + '[' + str(index) + ITEM)



