#!/usr/bin/env python

import companies
import helpers

class StockValue:

  def is_symbol_exists(self, symbol):
    return False if 'stockvalue' not in companies.companies[symbol] else True

  def set_stock_value(self, symbol, value):
    if 'stockvalue' not in companies.companies[symbol]:
      companies.companies[symbol]['stockvalue'] = value

  def process_stock_value(self, symbol):
    if not self.is_symbol_exists(symbol):
      sv = self.read_stock(symbol)
      self.set_stock_value(symbol, sv)
      return True
    return


  def get_stock_value(self, symbol):
    if 'stockvalue' not in companies.companies[symbol]:
      return companies.companies[symbol]['stockvalue']
    else:
      return 


  def read_stock(self, symbol):
    print "\nEnter stock value of " + symbol
    sv = raw_input()
    helpers.is_valid_int(sv)
    return sv

