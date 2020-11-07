import os
import unittest

from selenium import webdriver


class BaseTest(unittest.TestCase):

  @classmethod
  def setUp(self):
    browser = self.get_browser()
    self.driver = self.start_browser(browser)
    self.driver.maximize_window()
    # self.driver.find_elements()

  def get_browser():
    try:
      return os.environ['BROWSER']
    except KeyError:
      return 'Chrome'

  def start_browser(name='chrome'):
    try:
      if name.lower() == 'chrome':
        return webdriver.Chrome()
      elif name.lower() == 'firefox' or name.lower() == 'ff':
        return webdriver.Firefox()
      elif name.lower() == 'opera' or name.lower() == 'op':
        return webdriver.Opera()
      elif name.lower() == 'edge':
        return webdriver.Edge(executable_path=r'D:\Hoc\5.Testing\lamthu\Pack1\Drivers\msedgedriver.exe')
      elif name.lower() == 'safari':
        return webdriver.Safari()
        pass
      elif name.lower() == 'phantomjs' or name.lower() == 'ptjs':
        pass
      else:
        print("Not found browser %s on this device" % (name))
    except Exception as msg:
      print('error occur at', str(msg))

  @classmethod
  def tearDown(self):
    try:
      self.driver.close()
      # self.driver.quit()
    except Exception as msg:
      print('error occur at:', str(msg))
