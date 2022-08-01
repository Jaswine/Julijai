from django.test import TestCase
# from base.logic import operations

def operations(a,b,c):
  if c == '+':
    return a+b
  if c == '-':
    return a-b

class LogicTestCase(TestCase):
  def test_plus(self):
    answer = operations(6,3,'+')
    self.assertEqual(9, answer)
    self.assertEqual(18, answer)