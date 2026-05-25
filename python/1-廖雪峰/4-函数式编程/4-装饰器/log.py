# /usr/bin/env python3
# -*- encoding : utf-8 -*-
def log(func):
  def wrapper(*arg,**kw):
    print('call %s():' % func.__name__)
    return func(*arg,**kw)
  return wrapper
@log
def now():
  print('2015-3-25')
now()

