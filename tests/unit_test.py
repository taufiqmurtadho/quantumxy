import unittest
import numpy as np
import sys

sys.path.append('../')

from src import quantumxy as qxy


class TestHamiltonian(unittest.TestCase):

    def test_MethodEquivalence(self):
        booleanList = [np.array_equal(qxy.method1_hamiltonian(2,1,i), qxy.method2_hamiltonian(2,1,i)) for i in range(2,11)]
        print(booleanList)
        self.assertTrue(all(booleanList))


if __name__ == '__main__':
    unittest.main()
