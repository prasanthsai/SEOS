import unittest

from order import Order
from orderlist import OrderList
from stockorder import StockOrder


class TestSEOS(unittest.TestCase):

  stockorder = StockOrder()

  def test_execute_order_first(self):
    order = Order('buy', 'ABC', 10, 10)
    orderlog_result = OrderList([order])
    self.assertEqual(str(orderlog_result), str(self.stockorder.execute_order(order)))
    
  def test_execute_order_second(self):
    order = Order('sell', 'XYZ', 15, 15)
    self.stockorder.execute_order(order)
    order = Order('sell', 'ABC', 13, 13)
    executed_result = self.stockorder.execute_order(order)
    expected_result = OrderList(
      [
        Order('buy', 'ABC', 10, 0),
        Order('sell', 'XYZ', 15, 15),
        Order('sell', 'ABC', 13, 3)
      ]
    )
    self.assertEqual(
      str(expected_result), 
      str(executed_result)
    )
    
  def test_execute_order_third(self):
    order = Order('buy', 'XYZ', 10, 10)
    self.stockorder.execute_order(order)
    order = Order('buy', 'XYZ', 8, 8)
    executed_result = self.stockorder.execute_order(order)
    expected_result = OrderList(
      [
        Order('buy', 'ABC', 10, 0),
        Order('sell', 'XYZ', 15, 0),
        Order('sell', 'ABC', 13, 3),
        Order('buy', 'XYZ', 10, 0),
        Order('buy', 'XYZ', 8, 3)
      ]
    )
    self.assertEqual(
      str(expected_result), 
      str(executed_result)
    )

if __name__ == '__main__':
  unittest.main()
