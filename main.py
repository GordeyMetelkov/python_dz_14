from task import *
import unittest


class TestUnitCheck(unittest.TestCase):


    def setUp(self):
        first = worker()
        second = worker()
        self.first = first
        self.second = second


    def test_eq(self):
        self.assertTrue(self.first.level == self.first.level)


    def test_not_eq(self):
        self.assertFalse(self.first.level != self.second.level)

    def test_is(self):
        self.assertFalse(self.first is self.second)

if __name__ == '__main__':
    unittest.main(verbosity=2)