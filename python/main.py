#!/usr/bin/env python

from stockorder import *

if __name__ == '__main__':

  stockorder = StockOrder()
  while True:
    orders = stockorder.read_orders()
    for order in orders:
      stockorder.execute_order(order)
    stockorder.prettyprint()
    print "\n\nPress ctrl-D to exit the script"

