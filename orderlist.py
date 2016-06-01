#!/usr/bin/env python

import helpers

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

    



class OrderList:

  def __init__(self):
    self.orderlist = []

  def __iter__(self):
    return iter(self.orderlist)

  def addorder(self, order):
    self.orderlist.append(order)
    return len(self.orderlist) - 1
  
  def addorders(self, orders):
    self.orderlist.extend(orders)
    return len(self.orderlist) - 1

  def update_element_at_index(self, index, element, value):
    return self.orderlist[index].update(element, value)

  def get_element_at_index(self, index, element):
    return self.orderlist[index].get(element)
  
  def prettyprint(self):
    print '\nResultant order list : \n'
    for order in self.orderlist:
      print order.pretify()

