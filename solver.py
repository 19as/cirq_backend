import cirq
import click
from cirq.contrib.qasm_import import circuit_from_qasm

@click.command()
@click.argument('qasm', type=click.Path(exists=True))
@click.argument('shots', type=int)
# @click.option('-c', '--chart', is_flag=True, help='Build chart')
# @click.option('-s', '--save', nargs=2, help='Path and filename to save')
@click.option('-sh', '--show', is_flag=True, help='Print result to console')

def main(qasm, shots, show) -> dict:
    with open(qasm, 'r') as f:
        qasm_str = f.read()
    circuit = circuit_from_qasm(qasm_str)
    circuit = measures(circuit)
    counts = process(circuit, shots)
    if show:
        print(counts.histogram(key = 1))
    print('done!')

def measures(circuit):
    if circuit.has_measurements() == False:
        circuit.measure_all()
    return circuit

def process(circuit, shots):
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=shots)
    return result

if __name__ == '__main__':
    main()