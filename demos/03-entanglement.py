from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, Aer, execute

q = QuantumRegister(2)
c = ClassicalRegister(2)
qc = QuantumCircuit(q, c)

qc.h(q[0])
qc.cx(q[0], q[1])

qc.measure(q, c)

backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend)
result = job.result()

print(result.get_counts(qc))
