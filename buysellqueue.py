#!/usr/bin/env python

import companies
import helpers


class BuySellQueue:

  def __init__(self):
    self.buy = companies.QueueElement('buy')
    self.sell = companies.QueueElement('sell')

  def peek_mutex(self, side, symbol):
    return getattr(self, helpers.get_mutex_side(side)).peek(symbol)

  def isempty_mutex(self, side, symbol):
    return getattr(self, helpers.get_mutex_side(side)).isempty(symbol)

  def pop_mutex(self, side, symbol):
    return getattr(self, helpers.get_mutex_side(side)).pop(symbol)

  def isempty(self, side, symbol):
    return getattr(self, side).isempty(symbol)

  def append(self, side, symbol, value):
    return getattr(self, side).append(symbol, value)

