# /usr/bin/env python
# -*- coding: utf-8 -*-
class Student(object):
  def init_(self,name,score,gender):
    self.__name = name
    self.__score = score
    self.__gender = gender
  def get_gender(self):
    return self.__gender
  def get_name(self):
    return self.__name
  def get_score(self):
    return self.__score
  def set_gender(self,gender):
    if gender == 'man' or gender == 'woman':
      self.__gender = gender
    else:
      raise ValueError('bad gender')
  def set_score(self,score):
    if score >= 0 and score <= 100:
      self.__score = score
    else:
      raise ValueError('bad score')
bart = Student('Bart Simpson', 59, 'man')
bart.print_score()
bart.get_score()
bart.set_score(100)
bart.print_score()
