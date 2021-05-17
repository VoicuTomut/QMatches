from .matrix import *

# Operators for Jordan-Wigner mapping
def get_c(nrq):
    x = []
    for i in range(nrq):
        x2 = X
        x21 = Y
        for k in range(i):
            x2 = np.kron(Z, x2)
            x21 = np.kron(Z, x21)
        for k in range(i + 1, nrq):
            x2 = np.kron(x2, I)
            x21 = np.kron(x21, I)
        x.append(x2)
        x.append(x21)
    return x


class COp:
    def __init__(self, size):
        self.size = size
        self.elements = get_c(size)
        self.label, self.coef = self.labels()
        self.etichet = self.et()

    def et(self):
        et = []
        for i in range(self.size * 2):
            et.append("c_" + str(i))
        return et

    def labels(self):
        labels = []
        coef = []
        for j in self.elements:
            l = []
            c = []
            x_j, x_label = pauli_decompose(j)
            for i in range(len(x_j)):
                if abs(x_j[i]) != 0:
                    l.append(x_label[i])
                    c.append(x_j[i])
            labels.append(l)
            coef.append(c)
        return labels, coef

    def info(self):
        print("size:", self.size)
        label = self.label
        coef = self.coef
        print("nr. elements:", len(label))
        print("\n")
        for i in range(len(label)):
            print("ethiket:", self.etichet[i])
            print("labels:", label[i])
            print("coef:", coef[i])
            print("matrix: \n", self.elements[i])
            print("#################################################")
