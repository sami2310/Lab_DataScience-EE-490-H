import unittest
from fibonacci import fibonacci

class testfibonacci(unittest.TestCase):

    def testhappyflow(self):
        assert((fibonacci(3)) == [0, 1, 1, 2, 3])
	
    def testedges(self):
        assert ((fibonacci(0)) == [0, 1] )
        assert ((fibonacci(1)) == [0, 1, 1] )

    def test_underzero(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)

