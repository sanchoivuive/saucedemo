from Pages.BasePage import BasePage
from Locators.ProductListPageLocators import ProductListPageLocators
from Objects.Item import Item
from Objects.Product import Product



class ProductListPage(BasePage):
  def __init__(self, driver):
    super().__init__(driver)

  def get_product_name(self):
    return self.get_text(ProductListPageLocators.ITEM_NAME)

  def get_product_desc(self):
    return self.get_text(ProductListPageLocators.ITEM_DESC)

  def get_product_price(self):
    return self.get_text(ProductListPageLocators.ITEM_PRICE)

  def get_product_img(self):
    return self.get_img_src(ProductListPageLocators.ITEM_IMG)

  def get_broken_img(self):
    return self.get_elements_size(ProductListPageLocators.BROKEN_IMAGE)

  def add_to_cart_1(self,idx):
    self.click(ProductListPageLocators.LABEL_BUTTON_ADD(idx))

  def remove_from_cart_1(self,idx):
    self.click(ProductListPageLocators.LABEL_BUTTON_REMOVE(idx))

  def get_button_add(self):
    return self.get_text(ProductListPageLocators.ITEM_BUTTON_ADD)

  def add_to_cart(self):
    self.click(ProductListPageLocators.ITEM_BUTTON_ADD)

  def get_button_remove(self):
    return self.get_text(ProductListPageLocators.ITEM_BUTTON_REMOVE)

  def remove_from_cart(self):
    self.click(ProductListPageLocators.ITEM_BUTTON_REMOVE)

  # def get_product_info(self):
  #   name = self.get_text(ProductListPageLocators.ITEM_NAME,)
  #   desc = self.get_text(ProductListPageLocators.ITEM_DESC)
  #   price = self.get_text(ProductListPageLocators.ITEM_PRICE)
  #   img_url = self.get_img_src(ProductListPageLocators.ITEM_IMG)
  #   button_add = self.get_text(ProductListPageLocators.ITEM_BUTTON_ADD)
  #   self.add_to_cart()
  #   button_remove = self.get_text(ProductListPageLocators.ITEM_BUTTON_REMOVE)
  #   return Item(name,desc,price,img_url,button_add,button_remove)

  def get_product_info(self,idx):
    name = self.get_text(ProductListPageLocators.LABEL_PRODUCT_NAME(idx))
    desc = self.get_text(ProductListPageLocators.LABEL_PRODUCT_DESC(idx))
    price = self.get_text(ProductListPageLocators.LABEL_PRODUCT_PRICE(idx))
    return Product(name,desc,price)
