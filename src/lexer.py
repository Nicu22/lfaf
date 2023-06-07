import re

class Lexer:
    def __init__(self, file):
        self.f = open(file, 'r')
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

        self.token_list = []

        self.unorganized_tokens = self.f.read().split()

    def tokenize(self):
        i = -1
        while i < len(self.unorganized_tokens)-1:
            i += 1
            if '.' in self.unorganized_tokens[i] and self.unorganized_tokens[i] != '.':
                
                pos = self.unorganized_tokens[i].index('.')
                self.unorganized_tokens.insert(i + 1, self.unorganized_tokens[i][:pos])
                self.unorganized_tokens.insert(i + 2, '.')
                
                if pos != len(self.unorganized_tokens[i])-1:
                    self.unorganized_tokens.insert(i + 3, self.unorganized_tokens[i][pos+1:])
                continue

            if ';' in self.unorganized_tokens[i] and self.unorganized_tokens[i] != ';':
                pos = self.unorganized_tokens[i].index(';')
                self.unorganized_tokens.insert(i + 1, self.unorganized_tokens[i][:pos])
                self.unorganized_tokens.insert(i + 2, ';')
                continue

            if self.unorganized_tokens[i] in self.grammar:
                self.token_list.append([self.grammar[self.unorganized_tokens[i]], self.unorganized_tokens[i]])
            elif self.unorganized_tokens[i].isnumeric():
                self.token_list.append(['numeric', self.unorganized_tokens[i]])
            else:
                self.token_list.append(['unknown', self.unorganized_tokens[i]])

        return self.token_list



    def regex_tokenize(self):  # Function to classify tokens using regular expressions
        for token in self.unorganized_tokens:
            category = self.categorize_token(token)  # Classify the token using the categorize_token function
            self.token_list.append([category, token])  # Add the classified token to the token_list

        return self.token_list  # Return the list of classified tokens

    def categorize_token(self, token):  # Function to classify a single token
        for pattern, category in self.grammar.items():  # Iterate through each pattern in the grammar
            if token.isnumeric():  # If the token is numeric, classify it as such
                return 'numeric'

            if re.match(pattern, token):  # If the token matches a pattern, classify it accordingly
                return category

        return 'unknown'  # If the token doesn't match any patterns, classify it as 'unknown'