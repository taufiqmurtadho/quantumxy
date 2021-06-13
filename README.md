# quantumxy
Python simulation of a quantum spin chain on a ring (1D chain periodic boundary condition) under a Hamiltonian with XY-interaction and external magnetic field

Main functions: method1_hamiltonian(h,J,N), method2_hamiltonian(h,J,N)

INPUT
h: magnetic field strength
J: nearest-neighbor interaction strength
N: System's size (integer)

OUTPUT
Hamiltonian matrix in the form of np.array

method1 computes the Hamiltonian by considering its action to the Pauli-Z basis states
method2 computes the Hamiltonian directly through kronecker product operation
