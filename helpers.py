#!/usr/bin/env python

def sidelist():
  return ['buy', 'sell']

def get_mutex_side(side):
  return 'buy' if side == 'sell' else 'sell'

def is_valid_side(side):
  return True if side in sidelist() else False

def is_valid_int(p):
  try:
    q = int(p)
    return True
  except ValueError:
    print "Invalid character supplied as a quantity. Please try again"
    return

def parse_int(p):
  return int(p) if is_valid_int(p) else False

def is_valid_order_parameters(side, company, quantity):
  return is_valid_side(side) and is_valid_int(quantity)
