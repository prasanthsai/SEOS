#!/usr/bin/env python

from collections import deque
from companylist import CompanyList

class QueueElement(CompanyList):

  def __init__(self, method):
    self.method = method
    CompanyList.__init__(
      self,
      {
        method : deque()
      }
    )

  def peek(self, symbol):
    return -1 if self.isempty(symbol) else self.getmethod(symbol, self.method)[0]

  def isempty(self, symbol):
    return True if len(self.getmethod(symbol, self.method)) == 0 else False

  def pop(self, symbol):
    return -1 if self.isempty(symbol) else self.getmethod(symbol, self.method).popleft()

  def append(self, symbol, value):
    self.getmethod(symbol, self.method).append(value)
