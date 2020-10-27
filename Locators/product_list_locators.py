from selenium.webdriver.common.by import By

class ProductListLocators(object):
  BROKEN_IMAGE = (By.XPATH, '//img[contains(@src, "jpgWithGarbageOnItToBreakTheUrl")]')
  CART_ITEM = "//div[@class='inventory_list']/div[@class='inventory_item']["

  #CACH CUA TIEN
  #def product_info(self,idx=1):
  idx = 1
  ITEM_NAME = (By.XPATH,"//div[@class='inventory_list']/div[@class='inventory_item'][1]//div[@class='inventory_item_name']")
  ITEM_IMG = (By.XPATH, "//div[@class='inventory_list']/div[@class='inventory_item']["+ str(idx) +"]//img[@class='inventory_item_img']")
  ITEM_DESC = (By.XPATH, "//div[@class='inventory_list']/div[@class='inventory_item']["+ str(idx) +"]//div[@class='inventory_item_desc']")
  ITEM_PRICE = (By.XPATH, "//div[@class='inventory_list']/div[@class='inventory_item']["+ str(idx) +"]//div[@class='inventory_item_price']")

  ITEM_BUTTON_ADD = (By.XPATH, "//div[@class='inventory_list']/div[@class='inventory_item'][" + str(idx) +"]//div/button[contains(@class, 'btn_primary') and contains(@class, 'btn_inventory')]")

  ITEM_BUTTON_REMOVE = (By.XPATH, "//div[@class='inventory_list']/div[@class='inventory_item'][" + str(idx) +"]//div/button[contains(@class, 'btn_secondary') and contains(@class, 'btn_inventory')]")
  
  CART_ICON = '//*[@id="shopping_cart_container"]/a'
  CART_AMOUNT = '//*[@id="shopping_cart_container"]/a/span'

  #casch khasc
  def LABEL_PRODUCT_NAME(idx=1):
    ITEM = "]//div[@class='inventory_item_name']"
    return (By.XPATH, (ProductListLocators.CART_ITEM) + str(idx) +ITEM)

  def LABEL_PRODUCT_DESC(idx=1):
    ITEM = "]//div[@class='inventory_item_desc']"
    return (By.XPATH, (ProductListLocators.CART_ITEM) + str(idx) +ITEM)

  def LABEL_PRODUCT_PRICE(idx=1):
    ITEM = "]//div[@class='inventory_item_price']"
    return (By.XPATH, (ProductListLocators.CART_ITEM) + str(idx) +ITEM)

  def LABEL_PRODUCT_IMG(idx=1):
    ITEM = "]//div[@class='inventory_item_img']//img"
    return (By.XPATH, (ProductListLocators.CART_ITEM) + str(idx) +ITEM)

  def LABEL_BUTTON_ADD(idx=1):
    ITEM = "]//button[text()='ADD TO CART']"
    return (By.XPATH, (ProductListLocators.CART_ITEM) + str(idx) + ITEM)

  def LABEL_BUTTON_REMOVE(idx=1):
    ITEM = "]//button[text()='REMOVE']"
    return (By.XPATH, (ProductListLocators.CART_ITEM) + str(idx) + ITEM)
