import unittest
from xFin.xfin.bond import *

class TestBond(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print "This setUpClass() method only called once."

    @classmethod
    def tearDownClass(cls):
        print "This tearDownClass() method only called once too."

    def setUp(self):
        print "do something before test.Prepare environment."

    def tearDown(self):
        print "do something after test.Clean up."

    def test_cur_bond_value(self):

        """
        Test method cur_bond_value(list)
        根据测试数据，最终的结果为0.75，即3/4.
        """
        
        self.assertEqual(0, cur_bond_value(0,0,0,0))


if __name__ == "__main__":
    unittest.main()
