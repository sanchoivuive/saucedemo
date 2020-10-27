class PageData():
  BASE_URL = 'https://www.saucedemo.com'
  PAGE_TITLE = 'Swag Labs'

class StandardUser():
  USERNAME = 'standard_user'
  PASSWORD = 'secret_sauce'

class FakeUser():
  USERNAME = 'tienaaa'
  PASSWORD = 'aaaaaaaaaa'
  VERIFIED_POINT_URL = 'https://www.saucedemo.com/inventory.html'
  VERIFIED_POINT_PAGE_TITLE = 'Swag Labs'

class ProblemUser():
  USERNAME = 'problem_user'
  PASSWORD = 'secret_sauce'
  VERIFIED_POINT_URL = 'https://www.saucedemo.com/inventory.html'
  VERIFIED_POINT_PAGE_TITLE = 'Swag Labs'

class PerformanceGlitchUser():
  USERNAME = 'performance_glitch_user'
  PASSWORD = 'secret_sauce'
  VERIFIED_POINT_URL = 'https://www.saucedemo.com/inventory.html'
  VERIFIED_POINT_PAGE_TITLE = 'Swag Labs'

class LockedoutUser():
  USERNAME = 'locked_out_user'
  PASSWORD = 'secret_sauce'
  VERIFIED_POINT_MESSAGE = 'Sorry, this user has been locked out.'

class InvalidLoginMessage():
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

class ItemInfo():
  NAME = 'Sauce Labs Backpack'
  DESC = 'carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection'
  PRICE = '$29.99'
  IMG_URL = 'https://www.saucedemo.com/img/sauce-backpack-1200x1500.jpg'
  BUTTON_ADD = 'ADD TO CART'
  BUTTON_REMOVE = 'REMOVE'
