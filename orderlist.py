#!/usr/bin/env python

import helpers

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

