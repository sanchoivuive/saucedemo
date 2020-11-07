from selenium.webdriver.common.by import By


class ProductListLocators(object):
  BROKEN_IMAGE = (By.XPATH, '//img[contains(@src, "jpgWithGarbageOnItToBreakTheUrl")]')
  CART_ITEM = '//div[@class="inventory_list"]/div[@class="inventory_item"]['
  CART_ITEM1 = (By.XPATH, '//div[@class="inventory_list"]/div[@class="inventory_item"]')

  MENU_HAMBURGER = (By.ID, 'menu_button_container')
  CART_ICON = (By.XPATH, '//*[@id="shopping_cart_container"]')
  CART_AMOUNT = (By.XPATH, '//*[@id="shopping_cart_container"]/a/span')

  def LABEL_PRODUCT_NAME(index):
    ITEM = ']//div[@class="inventory_item_name"]'
    return (By.XPATH, (ProductListLocators.CART_ITEM) + str(index) + ITEM)

  def LABEL_PRODUCT_DESC(index):
    ITEM = ']//div[@class="inventory_item_desc"]'
    return (By.XPATH, (ProductListLocators.CART_ITEM) + str(index) + ITEM)

  def LABEL_PRODUCT_PRICE(index):
    ITEM = ']//div[@class="inventory_item_price"]'
    return (By.XPATH, (ProductListLocators.CART_ITEM) + str(index) + ITEM)

  def LABEL_PRODUCT_IMG(index):
    ITEM = ']//div[@class="inventory_item_img"]//img'
    return (By.XPATH, (ProductListLocators.CART_ITEM) + str(index) + ITEM)

  def LABEL_BUTTON_ADD(index):
    ITEM = ']//button[text()="ADD TO CART"]'
    return (By.XPATH, (ProductListLocators.CART_ITEM) + str(index) + ITEM)

  def LABEL_BUTTON_REMOVE(index):
    ITEM = ']//button[text()="REMOVE"]'
    return (By.XPATH, (ProductListLocators.CART_ITEM) + str(index) + ITEM)
