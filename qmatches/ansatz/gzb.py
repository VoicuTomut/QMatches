from qmatches.gates import GZB


def gzb_ansatz_cell(qc, nr_o, nr_e, thetas, hidden=False):

    """
    qc: QuantumCircuit(qo,name='ansatz_cell')
    nr_o: number of orbitals in qo
    nr_e: number of electrons /particles
    thetas: string of parameters
    """

    it = 0
    start = nr_e - 1
    limit = nr_o
    while start != -1:
        cq = start
        tq = start + 1
        while tq < limit:
            if hidden:
                qc.append(GZB(thetas[it]).gate, [cq, tq])
            else:
                GZB(thetas[it]).ad_to(qc, cq, tq)
            cq = cq + 1
            tq = tq + 1
            it = it + 1

        start = start - 1
        limit = limit - 1


    return qc
