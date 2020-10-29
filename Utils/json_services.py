import json
from collections import namedtuple
import json
from types import SimpleNamespace
# def read_list_product():
#   # with open('listProducts.json') as f:
#   data = json.load(f)
# return data
class JsonServices(object):

  def json_to_list_object(path,key,object_class_name):
    list_object = []
    with open(path, mode='r') as f:
      list_data = json.load(f).get(key)

      for i in range(len(list_data)):
        new_object = namedtuple(object_class_name, list_data[i].keys())(*list_data[i].values())
        list_object.append(new_object)
    return list_object
