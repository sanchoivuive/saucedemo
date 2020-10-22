from Pages.BasePage import BasePage
from Locators.ProductListPageLocators import ProductListPageLocators


class ProductListPage(BasePage):
  def __init__(self, driver):
    super().__init__(driver)

  def get_header_title(self):
    return self.get_text(ProductListPageLocators.HEADER_TITLE)

  def get_url(self):
    return self.driver.current_url

  def get_message(self):
    return self.get_text(ProductListPageLocators.LABEL_MESSAGE)