from selenium.webdriver.common.by import By

class ProductListPageLocators(object):
  # LABEL_MESSAGE = (By.XPATH, '//*[@id="login_button_container"]/div/form/h3')
  HEADER_TITLE = (By.ID,'inventory_filter_container')
  PAGE_ROUTER = '/inventory.html'