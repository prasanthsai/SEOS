#!/usr/bin/env python

class Order(object):

  side = ''
  company = ''
  quantity = ''
  remaining_quantity = ''
  
  def __init__(self, side = '', company = '', quantity = 0, remaining_quantity = 0):
    self.side = side
    self.company = company
    self.quantity = quantity
    self.remaining_quantity = remaining_quantity

  def update(self, element, value):
    setattr(self, element, value)
    return value

  def get(self, element):
    return getattr(self, element)

  def status(self):
    return 'Open' if self.remaining_quantity > 0 else 'Closed'
  
  def pretify(self):
    return str(self.side) + '\t' + \
      str(self.company) + '\t' + \
      str(self.quantity) + '\t' + \
      str(self.remaining_quantity) + '\t' + \
      str(self.status())

