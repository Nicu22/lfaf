# Define a class called Lexer
class Lexer:
    # Constructor to initialize the object with a file
    def __init__(self, file):
        # Open the file for reading
        self.f = open(file, 'r')
        # Define a grammar dictionary that maps tokens to their respective categories
        self.grammar = {
            'BEGIN': 'keywords',
            'END': 'keywords',
            'INPUT': 'keywords',
            'OUTPUT': 'keywords',
            'RAM': 'keywords',
            'I': 'variables',
            'Q': 'variables',
            'M': 'variables',
            'AND': 'logic gates',
            'OR': 'logic gates',
            'XOR': 'logic gates',
            'NOT': 'logic gates',
            'CN01': 'contacts',
            'CN02': 'contacts',
            'CN03': 'contacts',
            'CN04': 'contacts',
            ':=': 'operators',
            ';': 'separators',
            '.': 'separators'
        }

        # Initialize an empty list to store the tokenized output
        self.token_list = []

        # Read the contents of the file and split it into tokens
        self.unorganized_tokens = self.f.read().split()

    # Define a method to tokenize the input
    def tokenize(self):
        # Initialize a counter variable to keep track of the current token being processed
        i = -1

        # Loop through all the tokens in the input
        while i < len(self.unorganized_tokens)-1:
            
            # Increment the counter variable
            i += 1

            # Check if the current token has a dot somewhere in the middle
            if '.' in self.unorganized_tokens[i] and self.unorganized_tokens[i] != '.':
                
                # If it does, split it into two tokens and insert them into the list
                pos = self.unorganized_tokens[i].index('.')
                self.unorganized_tokens.insert(i + 1, self.unorganized_tokens[i][:pos])
                self.unorganized_tokens.insert(i + 2, '.')
                
                # If there are characters after the period, insert them as a separate token
                if pos != len(self.unorganized_tokens[i])-1:
                    self.unorganized_tokens.insert(i + 3, self.unorganized_tokens[i][pos+1:])
                continue

            # Check if the current token is an endline semicolon
            if ';' in self.unorganized_tokens[i] and self.unorganized_tokens[i] != ';':
                # If it is, split it into two tokens and insert them into the list
                pos = self.unorganized_tokens[i].index(';')
                self.unorganized_tokens.insert(i + 1, self.unorganized_tokens[i][:pos])
                self.unorganized_tokens.insert(i + 2, ';')
                continue

            # If the current token is a known keyword or operator, add it to the token list with its category
            if self.unorganized_tokens[i] in self.grammar:
                self.token_list.append([self.grammar[self.unorganized_tokens[i]], self.unorganized_tokens[i]])
            # If the current token is a numeric value, add it to the token list with the category 'numeric'
            elif self.unorganized_tokens[i].isnumeric():
                self.token_list.append(['numeric', self.unorganized_tokens[i]])
            # If the current token is unknown, add it to the token list with the category 'unknown'
            else:
                self.token_list.append(['unknown', self.unorganized_tokens[i]])

        # Return the token list
        return self.token_list


# Create an instance of the Lexer class with the specified file as input
NewLexer = Lexer('code.txt')
# Tokenize the input and store the output in a variable called tokens
tokens = NewLexer.tokenize()

print(tokens)