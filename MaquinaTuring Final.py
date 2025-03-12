#Valentina Montenegro Quevedo / Laura Valeria Vargas Gomez / Juan Sebastian Acosta

import math

class TuringMachine:
    def __init__(self, states, input_alphabet, tape_alphabet, initial_state, blank_symbol, final_states, transition_function):
        self.states = states
        self.input_alphabet = input_alphabet
        self.tape_alphabet = tape_alphabet
        self.state = initial_state
        self.blank_symbol = blank_symbol
        self.final_states = final_states
        self.transition_function = transition_function
        self.tape = []
        self.head = 0

    def reading_writing(self):

        if self.state in self.final_states:
            return False

        symbol = self.tape[self.head]
        if (self.state, symbol) not in self.transition_function:
            return False

        self.state, symbol, move = self.transition_function[(self.state, symbol)]

        self.tape[self.head] = symbol

        if move == 'R':
            self.head += 1
        elif move == 'L':
            self.head -= 1

        return True

    def run(self, input_string):
        self.tape = list(input_string) + [self.blank_symbol]
        self.head = 0

        while self.reading_writing():
            pass
        return ''.join(self.tape).strip(self.blank_symbol)

def limpiar_entrada(entrada):

    return '1' * int(entrada)

def limpiar_salida(salida):
    negativo = "-" in salida
    valor = salida.replace("+", "").replace("-", "").replace("_", "").count("1")
    return -valor if negativo else valor

def suma(x, y):
    maquina_turing = TuringMachine(
            {'q0', 'q1', 'q2', 'q3'},
            {'+', '1'},
            {'+', '1', '_'},
            'q0',
            '_',
            {'q3'},
            {
                ('q0', '1'): ('q0', '1', 'R'),
                ('q0', '+'): ('q1', '1', 'R'),
                ('q1', '1'): ('q1', '1', 'R'),
                ('q1', '_'): ('q2', '_', 'L'),
                ('q2', '1'): ('q2', '_', 'S'),
            }
        )

    output = maquina_turing.run(f"{limpiar_entrada(x)}+{limpiar_entrada(y)}")
    return limpiar_salida(output)

def resta(x, y):
    maquina_turing_resta = TuringMachine(
        {"q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10", "q11", "q12", "q13", "q14", "q15"},
        {'-', '1'},
        {'-', '1', '_', '0'},
        'q0',
        '_',
        {'q2', 'q6', 'q10'},
        {
            ('q0', '-'): ('q1', '-', 'R'),
            ('q1', '1'): ('q2', '1', 'S'),
            ('q1', '_'): ('q3', '_', 'L'),
            ('q3', '-'): ('q4', '-', 'L'),
            ('q4', '_'): ('q5', '_', 'R'),
            ('q5', '-'): ('q6', '0', 'S'),
            ('q0', '1'): ('q7', '1', 'R'),
            ('q7', '1'): ('q7', '1', 'R'),
            ('q7', '-'): ('q8', '-', 'R'),
            ('q8', '_'): ('q9', '_', 'L'),
            ('q9', '-'): ('q10', '_', 'S'),
            ('q8', '1'): ('q11', '1', 'R'),
            ('q11', '1'): ('q11', '1', 'R'),
            ('q11', '_'): ('q12', '_', 'L'),
            ('q12', '1'): ('q13', '_', 'L'),
            ('q13', '1'): ('q13', '1', 'L'),
            ('q13', '-'): ('q14', '-', 'L'),
            ('q14', '1'): ('q14', '1', 'L'),
            ('q14', '_'): ('q15', '_', 'R'),
            ('q15', '1'): ('q0', '_', 'R'),
        }
    )
    output = maquina_turing_resta.run(f"{limpiar_entrada(x)}-{limpiar_entrada(y)}")
    return limpiar_salida(output)

def multiplicacion(x, y):
    resultado = 0
    for _ in range(y):
        resultado = suma(resultado, x)
    return resultado

def division(x, y):
    cociente = 0
    while x >= y:
        x = resta(x, y)
        cociente = suma(cociente, 1)
    return cociente

def potencia(x, y):
    resultado = 1
    for _ in range(y):
        resultado = multiplicacion(resultado, x)
    return resultado

def raiz(x):
    i = 0
    while multiplicacion(i, i) <= x:
        i = suma(i, 1)
    return resta(i, 1)

def ln(x):
    iteracion = 0
    while x >= 3:
        x = division(x, 3)
        iteracion = suma(iteracion, 1)
    return iteracion

def sin(x, precision = 10):
    resultado = 0
    signo = 1
    for n in range(precision):
        exponente = suma(multiplicacion(2, n), 1)
        factorial_val = math.factorial(exponente)
        potencia_val = potencia(x, exponente)
        termino = division(potencia_val, factorial_val)
        if n % 2 == 1:
            termino = resta(0, termino)
        resultado = suma(resultado, termino)
    return resultado