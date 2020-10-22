from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

  def verify_title(self, expected_title):
    # return title in self.get_title()
    try:
      return WebDriverWait(self.driver, self.timeout).until(EC.title_contains(expected_title))
    except self.timeout as e:
      print('error occur at:', str(e))

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
