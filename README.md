# quantumxy
Python simulation of a 1D quantum spin chain on a ring under a Hamiltonian with XY-interaction and external magnetic field

## FUNCTION  
```method1_hamiltonian(h,J,N)```: Constructing the Hamiltonian by its action toward Pauli-Z basis states
```method2_hamiltonian(h,J,N)```:Constructing the Hamiltonian by direct kronecker product

where h is magnetic field strength, J is nearest-neighbor interaction strength, and N is system's size (integer). The output of these functions is a ```numpy``` array of size 2^N x 2^N. 

## Setup

In the package directory, run the following command

```pip install``` 

To use, type ```import src.quantumxy``` in the Python shell
