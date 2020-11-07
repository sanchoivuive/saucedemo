import re


class Utilities:

  def get_number(string):
    try:
      return float(re.findall('\d+\.\d+', string)[0])
    except:
      return 0.0


  def calculate_tax(subtotal, tax_rate=0.08):
    tax = round(subtotal * tax_rate, 2)
    return tax

  def calculate_total(subtotal,tax):
    total = subtotal + tax
    return round(total,2)

