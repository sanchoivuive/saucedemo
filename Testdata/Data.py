class PageData():
  BASE_URL = 'https://www.saucedemo.com'
  PAGE_TITLE = 'Swag Labs'

class StandardUser():
  USERNAME = 'standard_user'
  PASSWORD = 'secret_sauce'
  VERIFIED_POINT_URL = 'https://www.saucedemo.com/inventory.html'

class ProblemUser():
  USERNAME = 'problem_user'
  PASSWORD = 'secret_sauce'

class InvalidLogin():
  INVALID_USER_MESSAGE = 'Username and password do not match any user in this service'
  USERNAME_REQUIRED_MESSAGE = 'Username is required'
  PASSWORD_REQUIRED_MESSAGE = 'Password is required'

class Browser():
  CHROME = 'Chrome'
  FIREFOX = 'Firefox'
  OPERA = 'Opera'
  EDGE = 'Edge'
  SAFARI = 'Safari'
  PHANTOMJS = 'PhantomJS'