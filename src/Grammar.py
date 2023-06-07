import random
from finiteAutomata import FiniteAutomata  
from cnf import CNFConvertor  
class RegularGrammar:
    
    def __init__(self,Vn,Vt,P,a):
        self.Vn = Vn  # Non-terminal symbols
        self.Vt = Vt  # Terminal symbols
        self.P = P  # Production rules
        self.alphabet = a  # Alphabet
        self.word_list = []  # Initializing list for generated words
        self.word = ''  # Initializing the word


    def GenerateWord(self):
        self.word_list = []
        self.word='S'
        self.word_list.append(self.word)
        while self.word[-1].isupper():
            aux = []
            aux.append(self.word[-1])
            self.word = self.word[:-1]+random.choice(self.P[self.word[-1]])
            if self.word[-1].isupper():
                aux.append(self.word[-2])
                aux.append(self.word[-1])
            else:
                aux.append(self.word[-1])
            self.word_list.append(aux)
        self.word_list=self.word_list[1:]
        print(f'generated word: {self.word}')
        print(f'used transitions for created word: {self.word_list}')
        return self.word

    def ConvertFA(self):
        initial_states =[]
        for state in self.P['S']:
            initial_states.append(state[0])
        transition_functions = []
        for key in self.P:
            for state in self.P[key]:
                aux = []
                aux.append(key)
                aux = aux + list(state)
                transition_functions.append(aux)
        print(f'valid transitions: {transition_functions}')
        automaton = FiniteAutomata(initial_states, self.Vt, self.alphabet, transition_functions, self.Vn)
        return automaton

    def chumsky_type(self):
        def upper_number(state):
            uppers = 0
            for letter in state:
                if letter.isupper():
                    uppers += 1
            return uppers
        def upper_pos(state):
            pos = 0
            for i in range(0, len(state)):
                if state[i].isupper():
                    pos=i
            if pos == len(state)-1:
                return -1
            return pos
        chum_type = 3
        return chum_type

    def ConvertCNF(self):
        chomsky_form = CNFConvertor(self.P, self.Vn)
        chomsky_form.Transform()
        return chomsky_form