from Locators.finish_locators import FinishLocators
from Pages.base_page import BasePage


class FinishPage(BasePage):
  def __init__(self, driver):
    super().__init__(driver)

  def get_header_title(self):
    return self.get_text(FinishLocators.HEADER_TITLE)

  def get_complete_title(self):
    return self.get_text(FinishLocators.COMPLETE_TITLE)

  def get_complete_message(self):
    return self.get_text(FinishLocators.COMPLETE_MESSAGE)

  def is_img_visible(self):
    return self.is_visible(FinishLocators.COMPLETE_IMG)
