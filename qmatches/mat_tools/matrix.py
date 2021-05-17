import numpy as np
import itertools

# Pauli matrix
I = np.array([[1, 0], [0, 1]], dtype=np.complex128)
X = np.array([[0, 1], [1, 0]], dtype=np.complex128)
Y = np.array([[0, -1.0j], [1.0j, 0]], dtype=np.complex128)
Z = np.array([[1, 0], [0, -1]], dtype=np.complex128)

pauli = [I, X, Y, Z]
labels = ["I", "X", "Y", "Z"]
indice = [0, 1, 2, 3]


def comutation(mat1, mat2):
    return np.matmul(mat1, mat2) - np.matmul(mat2, mat1)


def corelation(dens, op):
    nrq = int(np.log2(len(dens)))
    x = op.elements
    cor = []
    for i in range(2 * nrq):
        li = []
        for j in range(2 * nrq):
            li.append((1.0j / 2) * np.matmul(comutation(x[i], x[j]), dens).trace())
        cor.append(li)
    return cor


# Make Hilbert Schmid product betwen matrices mat1 and mat2
def hilbert_schmid(mat1, mat2):
    return (np.dot(mat1.conjugate().transpose(), mat2)).trace()


# Pauli decomposition:
# Decompose  observable in matrices create by kron. product o Pauli matrices
# (h-coeficient , h_label-kron product structure )


def pauli_decompose(obs):
    size = len(obs)
    nr_pauli = np.log2(size)
    norm_fact = 1 / (2 ** nr_pauli)

    elements = itertools.product(indice, repeat=int(nr_pauli))
    h_label = []
    h = []
    for i in elements:
        label = ""
        matrice = pauli[i[0]]
        for j in i:
            label = label + labels[indice[j]]
        for j in range(int(nr_pauli) - 1):
            matrice = np.kron(matrice, pauli[i[j + 1]])
        # print(matrice)
        h_label.append(label)
        h.append(norm_fact * hilbert_schmid(matrice, obs))

    return h, h_label


def print_paili_decompose(mat):
    c, l = pauli_decompose(mat)
    for i in range(len(l)):
        if abs(c[i]) >= 0.00000000001:
            print("{}:{}".format(l[i], c[i]))
