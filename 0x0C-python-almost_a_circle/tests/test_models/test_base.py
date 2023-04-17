#!/usr/bin/python3

import unittest
from models.base import Base

class BaseTest(unittest.Testcase):

	def test_func_1(self):
		#Arrange
		b1 = Base()

		#Act

		#Assert

		self.assertEqual(b1.id, 1)






if __name__ == "__main__":
    unittest.main()
