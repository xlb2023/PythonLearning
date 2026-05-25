# /usr/bin/env python
# -*- conding: utf-8 -*-
class Student(object):
  def __init__(self,name,score):
    self._name = name
    self._score = score
  def print_score(self):
    print('%s: %s' % (self._name,self._score))
  def get_grade(self):
    if self._score >= 90:
      return 'Grade A'
    elif self._score >= 60:
      return 'Grade B'
    else:
      return 'Grade C'
  def get_name(self):
    return self._name
  def get_score(self):
    return self._score
  def set_score(self,score):
    if score >= 0 and score<=100:
      self._score = score
    else:
      raise ValueError('bad score')
bart = Student('Bart Simpson', 59)
bart.print_score()
bart.get_score()
bart.set_score(100)
bart.print_score()
bart.__name = 'New Name'
print(bart.__name)
print(bart.get_name())