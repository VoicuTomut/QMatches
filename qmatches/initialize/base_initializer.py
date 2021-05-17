import numpy as np
from qiskit import QuantumCircuit


class init_xo:
    # class for initalial states of the form: 000, 100, 110, 111

    def __init__(self, nrq, nr_e):
        # nrq-total number of qbits
        # x_qubit-nr of qubits in state 1
        self.nrq = nrq
        self.nr_e = nr_e
        self.density = self.densit()

    def densit(self):
        nrq = self.nrq
        nr_e = self.nr_e
        density = np.zeros((2 ** nrq, 2 ** nrq))
        token = 0
        for i in range(nr_e):
            token = token + 2 ** i
        density[token][token] = 1
        return density

    def citcuit(self):
        circ = QuantumCircuit(self.nrq)
        for i in range(self.nr_e):
            circ.x(i)
        return circ
