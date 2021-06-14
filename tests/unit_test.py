import unittest
import numpy as np
import numpy.linalg as la
import sys

sys.path.append('../')

from src import quantumxy as qxy

class TestHamiltonian(unittest.TestCase):

#Check that method1 and method2 gives the same result for varying system's size (N = 2-5):
    def test_MethodEquivalence(self):
        booleanList = [np.array_equal(qxy.method1_hamiltonian(2,1,i), qxy.method2_hamiltonian(2,1,i)) for i in range(2,6)]
        self.assertTrue(all(booleanList))

#Check that for J = 0, h>0 the ground state is all up state
    def test_ZeroCoupling1(self):
        eigval, eigvec = la.eigh(qxy.method1_hamiltonian(2,0,3))
        groundState = eigvec[:,eigval.argsort()][0]
        self.assertTrue(np.array_equal(groundState.T, np.array([1,0,0,0,0,0,0,0])))

#Check that for J = 0, h<0 the ground state is all down state
    def test_ZeroCoupling2(self):
        eigval, eigvec = la.eigh(qxy.method1_hamiltonian(-2,0,3))
        groundState = eigvec[:,eigval.argsort()][0]
        self.assertTrue(np.array_equal(groundState.T, np.array([0,0,0,0,0,0,0,1])))

#Allow user to directly run the test by python unit_test.py
if __name__ == '__main__':
    unittest.main()
