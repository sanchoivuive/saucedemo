import re
class StringToNumber():
  def get_number(self,string):
    try:
      return re.findall('\d+\.\d+', string)[0]
    except:
      return 0.0