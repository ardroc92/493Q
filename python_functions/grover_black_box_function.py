from qiskit import QuantumCircuit, QuantumRegister
import numpy as np

def U_f(circ_global, qubits):
    ##### OR gate #####
    
    
    # Build a sub-circuit
    #sub_q = QuantumRegister(n+m)
    circ = QuantumCircuit(5, name='U_f')
    
    
    circ.x(0)
    circ.x(1)
    
    circ.x(4)
    circ.ccx(0,1,4)
    circ.x(4)
    
    circ.ccx(2,4,3)
    
    circ.x(4)
    circ.ccx(0,1,4)
    circ.x(4)
    
    circ.x(1)
    circ.x(0)
    
    
    ##############

    sub_inst = circ.to_instruction()
    
    q = circ_global.qubits
    circ_global.append(sub_inst, [q[qubits[i]] for i in range(len(qubits))])



