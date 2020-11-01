import json
from objects.product import Product
class TestData():
  FILE = 'testdata\\listProducts.json'

  def getProducts(self):
    products = []
    with open(TestData.FILE) as json_file:
      data = json.load(json_file)
      for item in data['products']:
        product = Product(item['name'], item['desc'], item['price'])
        products.append(product)
      json_file.close()

    return products