import numpy as np
from itertools import product

#List of Parameters:
#h is the magnetic field strength
#J is the coupling strength between nearest neighbor sites
#N is the system's size

#Constructing the Hamiltonian matrix by considering its action towards sigma-z basis states
def method1_hamiltonian(h, N):
    mat = np.zeros((2**N,2**N))
    bitsequence = [list(x) for x in product([1,0],repeat =N)]
    for sequence in bitsequence:
        if sequence[N-1]!=sequence[0]:                                  #periodic boundary condition
            newseq = sequence.copy()
            newseq[N-1] = sequence[0]; newseq[0] = sequence[N-1]
            mat[bitsequence.index(sequence), bitsequence.index(newseq)]+= -1
        for i in range(N-1):
            if sequence[i]!=sequence[i+1]:
                newseq = sequence.copy()
                newseq[i] = sequence[i+1]; newseq[i+1]=sequence[i]
                mat[bitsequence.index(sequence), bitsequence.index(newseq)]+=-1
    for i in range(2**N):
        mat[i,i] = h*sum(bitsequence[i])-h*(N - sum(bitsequence[i]))
    return mat

#Constructing the Hamiltonian matrix by kronecker product
def method2_hamiltonian(h,N):
    pauli_plus = np.array([[0,1],[0,0]])
    pauli_minus = np.array([[0,0],[1,0]])
    pauliz = np.array([[1,0],[0,-1]])
    mat = np.zeros((2**N, 2**N))
    for i in range(N):
        if i == 0:
            hopping = -np.kron(np.kron(pauli_plus, pauli_minus),np.identity(2**(N-2)))
            mat+= h*np.kron(pauliz, np.identity(2**(N-1)))
            mat+=hopping+np.conj(hopping.T)
        elif i == N-1:                                                      #periodic boundary condition
            hopping = -np.kron(np.kron(pauli_minus, np.identity(2**(N-2))), pauli_plus)
            mat+= h*np.kron(np.identity(2**(N-1)), pauliz)
            mat+= hopping+np.conj(hopping.T)
        else:
            hopping = -np.kron(np.kron(np.identity(2**i), np.kron(pauli_plus, pauli_minus)), np.identity(2**(N-i-2)))
            mat+= h*np.kron(np.kron(np.identity(2**i),pauliz), np.identity(2**(N-i-1)))
       return mat 
