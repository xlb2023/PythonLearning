# /usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
  def __init__(self,name,score):
    self.name = name
    self.score = score
  def print_score(self):
    print('%s: %s' % (self.name,self.score))
  def get_grade(self):
    if self.score >= 90:
      return 'Grade A'
    elif self.score >= 60:
      return 'Grade B'
    else:
      return 'Grade C'
lisa = Student('Lisa', 99)
lisa.print_score()
print(lisa.get_grade())