from selenium.webdriver.common.by import By


class FinishLocators(object):
  HEADER_TITLE = (By.XPATH,'//*[@id="contents_wrapper"]/div[@class="subheader"]')
  COMPLETE_TITLE = (By.XPATH,'//*[@id="checkout_complete_container"]/h2[@class="complete-header"]')
  COMPLETE_MESSAGE = (By.XPATH,'//*[@id="checkout_complete_container"]/div[@class="complete-text"]')

  COMPLETE_IMG = (By.XPATH,'//*[@id="checkout_complete_container"]/img[@class="pony_express"]')
