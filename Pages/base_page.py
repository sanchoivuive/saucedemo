from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

class BasePage(object):
  def __init__(self, driver):
    self.driver = driver
    self.timeout = 30

  # Common element of a page
  def navigate_url(self, url):
    self.driver.get(url)

  def get_title(self):
    return self.driver.title

  def get_url(self):
    return self.driver.current_url

  # Common inspect elements on a page
  def click(self, locator):
    WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator)).click()

  def enter_text(self, locator, text):
    input_field = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
    input_field.clear()
    input_field.send_keys(text)

  def get_text(self, locator):
    element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
    return element.text

  def get_elements_size(self,locator):
    WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
    elements = self.driver.find_elements(*locator)
    return len(elements)

  def is_visible(self,locator):
    element = WebDriverWait(self.driver, self.timeout).until(
      EC.visibility_of_element_located(locator))
    # print(element.is_displayed())
    return bool(element.is_displayed())

  def is_enabled(self, by_locator):
    message = "Check the element with the locator '{}' is enabled or not"
    logging.info(message.format(','.join(by_locator)))

    element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))
    return element.is_enabled()

  def is_element_existed(self,locator):
    existed = True
    try:
      WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
    except Exception:
      existed = False
    return existed

  def is_invisible(self, by_locator):
    message = "Check the element with the locator '{}' is visible or not"
    logging.info(message.format(','.join(by_locator)))

    flag = False
    try:
      element = self.driver.find_element(by_locator)
      element.is_displayed()
    except:
      flag = True
      pass

    return flag