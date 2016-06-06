#!/usr/bin/env python
import copy

companies = {}
company_methods = {}

def add_method_to_companies(method_name, method_value):
  if not company_methods.has_key(method_name):
    company_methods[method_name] = copy.copy(method_value)
  for symbol in companies:
    add_method_to_company(symbol, method_name, method_value)

def add_company(symbol):
  if not companies.has_key(symbol):
    companies[symbol] = {}
  for method, value in company_methods.iteritems():
    add_method_to_company(symbol, method, value)

def add_method_to_company(symbol, method, value):
  if method not in companies[symbol]:
    companies[symbol][method] = copy.copy(value)


class CompanyList:

  def __init__(self, methods = {}):
    self.methods = methods
    self._add_methods_to_companies(methods)

  def add(self, symbol):
    add_company(symbol)

  def exists(self, symbol):
    return companies.has_key(symbol)

  def updatemethod(self, symbol, method, value):
    if not self.exists(symbol):
      self.add(symbol)
    companies[symbol][method] = value

  def getmethod(self, symbol, method):
    if self.exists(symbol):
      return companies[symbol][method]
    else:
      return

  def _add_methods_to_companies(self, methods):
    for method, value in methods.iteritems():
      add_method_to_companies(method, value)
    return
