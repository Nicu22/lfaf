# Importing necessary classes from modules
from Grammar import RegularGrammar
from finiteAutomata import FiniteAutomata


# Defining a dictionary representing a context-free grammar
p = {
    'S':['aA'],
    'A':['bS','aB'],
    'B':['bC','aBB'],
    'C':['aA','b'],
} 

# Defining the non-terminals and terminals of the grammar
vn = ['S','A','B','C']
vt = ['a','b']
a = vt


new_grammar = RegularGrammar(vn,vt,p,a)
new_automaton = new_grammar.ConvertFA()


for i in range(5):
    new_grammar.GenerateWord()
    new_grammar.ConvertFA()
    print()
    word = new_grammar.GenerateWord()
    if new_automaton.checkWord(word):
        print('Valid word')
    print()

user_word = 'abbbbaaaabbb'
if new_automaton.checkWord(user_word):
    print('user word is valid')
else:
    print('user word not valid')