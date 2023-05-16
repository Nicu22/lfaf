import random
from finiteAutomata import FiniteAutomata

class RegularGrammar:
    def __init__(self, Vn, Vt, P, a):
        self.Vn = Vn       # Non-terminal symbols
        self.Vt = Vt       # Terminal symbols
        self.P = P         # Production rules
        self.alphabet = a  # Alphabet
        self.word_list = []  # List to store generated words
        self.word = ''       # Current word being generated


    # Defining the GenerateWord method
    def GenerateWord(self):
        self.word_list = []  # Reset the word list
        self.word = 'S'  # Set the initial word to 'S'
        self.word_list.append(self.word)  # Add the initial word to the word list
        
        # Continue generating words until the last character of the word is not uppercase
        while self.word[-1].isupper():
            aux = []  # Temporary list to store information about the current transition
            aux.append(self.word[-1])  # Add the current non-terminal symbol to the transition list
            
            # Generate the next character of the word based on the production rules
            self.word = self.word[:-1] + random.choice(self.P[self.word[-1]])
            
            if self.word[-1].isupper():
                aux.append(self.word[-2])  # Add the previous non-terminal symbol to the transition list
                aux.append(self.word[-1])  # Add the current non-terminal symbol to the transition list
            else:
                aux.append(self.word[-1])  # Add the current terminal symbol to the transition list
            
            self.word_list.append(aux)  # Add the transition list to the word list
        
        self.word_list = self.word_list[1:]  # Remove the initial word from the word list
        print(f'generated word: {self.word}')  # Print the generated word
        print(f'used transitions for created word: {self.word_list}')  # Print the transitions used to create the word
        return self.word  # Return the generated word

    # Defining the ConvertFA method
    def ConvertFA(self):
        initial_states = []  # List to store initial states
        for state in self.P['S']:
            initial_states.append(state[0])  # Add the first element of each production rule for 'S' to the initial states list

        transition_functions = []  # List to store transition functions
        for key in self.P:
            for state in self.P[key]:
                aux = []  # Temporary list to store a transition function
                aux.append(key)  # Add the key (non-terminal symbol) to the transition function
                aux = aux + list(state)  # Add the elements of the state (terminal and non-terminal symbols) to the transition function
                transition_functions.append(aux)  # Add the transition function to the list of transition functions

        print(f'valid transitions: {transition_functions}')  # Print the valid transitions

        # Create a FiniteAutomata object using the collected information
        automaton = FiniteAutomata(initial_states,
                                self.Vt,
                                self.alphabet,
                                transition_functions,
                                self.Vn)
        return automaton  # Return the created automaton



    # Defining the chumsky_type method
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
                    pos = i
            if pos == len(state) - 1:
                return -1
            return pos

        chum_type = 3  # Default value for the Chomsky type

        # Check for Chomsky type 1 and empty states
        for key in self.P:
            if len(key) >= 2:
                chum_type = 1
            for state in self.P[key]:
                if state == '' and chum_type == 1:
                    return 0  # Return 0 if there is an empty state and Chomsky type is 1

        if chum_type == 1:
            return 1  # Return 1 if Chomsky type is 1

        # Check for Chomsky type 2
        for key in self.P:
            for state in self.P[key]:
                if upper_number(state) > 1:
                    return 2  # Return 2 if there is more than one uppercase letter in a state
                elif upper_number(state) == 1:
                    location = upper_pos(state)  # Get the position of the uppercase letter

        # Check for Chomsky type 3
        for key in self.P:
            if upper_number(self.P[key][0]) > 1:
                return 2  # Return 2 if the first state has more than one uppercase letter
            if upper_pos(self.P[key][0]) not in [0, -1]:
                return 2  # Return 2 if the position of the uppercase letter in the first state is not 0 or -1
            for i in range(1, len(self.P[key])):
                if not self.P[key][i].islower() and self.P[key][i] != '':
                    if upper_number(self.P[key][i]) > 1:
                        return 2  # Return 2 if a non-initial state has more than one uppercase letter
                    if upper_pos(self.P[key][i]) != upper_pos(self.P[key][i - 1]):
                        return 2  # Return 2 if the position of the uppercase letter changes between consecutive states

        return chum_type  # Return the Chomsky type (default is 3 if not determined as type 1 or 2)

