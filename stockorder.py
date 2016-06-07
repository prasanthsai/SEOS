#!/usr/bin/env python

import companies
import helpers
from buysellqueue import BuySellQueue
from order import *
from orderlist import *


class StockOrder:

  def __init__(self):
    self.buysellqueue = BuySellQueue()
    self.orderlog = OrderList()

  def execute_order(self, order):
    companies.add_company(order.company)
    while True:
      mutex_remaining_quantity = self._get_mutex_remaining_quantity(order.side, order.company)
      if not mutex_remaining_quantity:
        self._log_order_with_append(order)
        break
      if not order.remaining_quantity:
        self._log_order(order)
        break

      if mutex_remaining_quantity > order.remaining_quantity:
        order = getattr(self, '_greater')(order, mutex_remaining_quantity)
      elif mutex_remaining_quantity < order.remaining_quantity:
        order = getattr(self, '_lower')(order, mutex_remaining_quantity)
      else:
        order = getattr(self, '_equal')(order, mutex_remaining_quantity)
    return self.orderlog



  def _greater(self, order, mutex_rq):
    self._set_mutex_remaining_quantity(order.side, order.company, mutex_rq - order.remaining_quantity)
    order.remaining_quantity = 0
    return order

  def _lower(self, order, mutex_rq):
    order.remaining_quantity = order.quantity - mutex_rq
    self._set_mutex_remaining_quantity(order.side, order.company, 0)
    self.buysellqueue.pop_mutex(order.side, order.company)
    return order

  def _equal(self, order, mutex_rq):
    order.remaining_quantity = 0
    self._set_mutex_remaining_quantity(order.side, order.company, 0)
    self.buysellqueue.pop_mutex(order.side, order.company)
    return order

  def _get_mutex_remaining_quantity(self, side, company):
    index = self.buysellqueue.peek_mutex(side, company)
    return self.orderlog.get_element_at_index(index, 'remaining_quantity') if index >= 0 else 0
  
  def _set_mutex_remaining_quantity(self, side, company, value):
    index = self.buysellqueue.peek_mutex(side, company)
    return self.orderlog.update_element_at_index(index, 'remaining_quantity', value)

  def _log_order(self, order):
    return self.orderlog.addorder(order)
  
  def _log_order_with_append(self, order):
    self.buysellqueue.append(order.side, order.company, self._log_order(order))

  def prettyprint(self):
    self.orderlog.prettyprint()

  def read_orders(self):
    entered_orders = OrderList()
    print "Note: Press enter after entering orders\n " + \
          "Enter order with space delimiter in following order:\n " + \
          "Side Company Quantity"
    while True:
      entered_list = raw_input().split()
      if len(entered_list) == 0:
        print "Recevied orders... Processing..."
        break
      if len(entered_list) != 3:
        print "Invalid format, Skipping it. Reenter in valid format"
        continue
      side, company, quantity = entered_list
      if not helpers.is_valid_order_parameters(side = side, company = company, quantity = quantity):
        print "Invalid format, Skipping it. Reenter in valid format"
        continue
      parsed_quantity = helpers.parse_int(quantity)
      entered_orders.addorder(
        Order(
          side = side,
          company = company,
          quantity = parsed_quantity,
          remaining_quantity = parsed_quantity
        )
      )
    return entered_orders
