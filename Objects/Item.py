class Item():
  def __init__(self,name,desc,price,imgUrl,add,remove):
    self.img_url = imgUrl
    self.name = name
    self.desc = desc
    self.price = price
    self.button_add = add
    self.button_remove = remove