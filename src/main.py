from lexer import Lexer
from parse import Parser


'''
#Variant 22:

# Defining a dictionary representing a context-free grammar
p = {
    'S' : ['dB', 'A'],
    'A' : ['d', 'dS', 'aAdAB'],
    'B' : ['aC', 'aS', 'AC'],
    'C' : [''],
    'E' : ['AS']
}

# Defining the non-terminals and terminals of the grammar
vn = ['S', 'A', 'B', 'C', 'E']
vt = ['a', 'd']
a = vt

'''

NewLexer = Lexer('code.txt')
tokens = NewLexer.regex_tokenize()
print(tokens)

new_parser = Parser(tokens)
new_parser.parse()