
# Parser & Building an Abstract Syntax Tree
### Course: Formal Languages & Finite Automata
### Author: Popescu Nichifor FAF-212
### Variant: 22
## Objectives
1.  Get familiar with parsing, what it is and how it can be programmed [1].
2.  Get familiar with the concept of AST [2].
3.  In addition to what has been done in the 3rd lab work do the following:
    1. In case you didn't have a type that denotes the possible types of tokens you need to:
        1.  Have a type  **_TokenType_**  (like an enum) that can be used in the lexical analysis to categorize the tokens.
        2.  Please use regular expressions to identify the type of the token.
    2.  Implement the necessary data structures for an AST that could be used for the text you have processed in the 3rd lab work.
    3.  Implement a simple parser program that could extract the syntactic information from the input text.

## Implementation description
Even while laboratory work 3 did not rely on regular expressions, it offered similar features. In this particular lab, a novel approach is presented to improve the Lexer class by integrating a method called as "regex_tokenize." In this novel approach, tokens are categorized using regular expressions, making use of the Python're' package. This innovative strategy gives the Lexer class more power and offers a new angle on the problem at issue. 

### Types of tokens
Suite, Test, and Order are the three categories, and each has a specific function within the script.
The Parser class has the following definition:
```
class  Parser:
	def  __init__(self, tokens):
		self.tokens  =  tokens
		self.current_token_index  =  0
		self.current_token  =  None

	def  parse(self):
		self.advance()
		self.parse_program()

	def  advance(self):
		if  self.current_token_index  <  len(self.tokens):
		self.current_token  =  self.tokens[self.current_token_index]
		self.current_token_index  +=  1
```
The parsing method begins with the parse method. To go on to the next token, it calls the advance method, and to parse the complete program, it calls the parse_program method.
By using the advance method, the parser advances to the following token in the list of tokens. It makes the appropriate adjustments to the current_token_index and current_token variables.
If the current token and the anticipated token type match, the match function returns true. If so, it uses the advance function to move on to the next token. If not, a Syntax Error is raised with the proper error message.



## Conclusion
In conclusion, the project I built in Python for parsing and building an Abstract Syntax Tree (AST) has been a significant accomplishment in the field of programming. By implementing a Parser class with various methods, I have successfully constructed a reliable and efficient system for processing input tokens and generating an accurate AST.

The project's foundation lies in the init function of the Parser class, where the input tokens are used to initialize the object. This allows for seamless integration of the token list into the parsing procedure. The parse method serves as the entry point, initiating the parsing process and guiding the progression through the token list.

To ensure proper parsing, the advance method plays a crucial role by advancing to the next token in the token list. This controlled progression enables the parser to navigate through the input tokens systematically. The match method serves as a critical tool for determining whether the current token matches the expected type. If a match is found, the parser moves forward; otherwise, a SyntaxError is raised to handle unexpected tokens.

The completeness of the program is ensured by the parse_program method, which orchestrates the parsing of different sections while verifying the presence of "BEGIN" and "END" keywords. The input section is parsed by the parse_input_section method, which handles variable declarations followed by a semicolon. Similarly, the parse_output_section method deals with variable declarations in the output section, maintaining the consistent structure of the program.

The parse_ram_section method addresses the parsing of the program's RAM section, encompassing contact, logic gate, variable, and numeric tokens. This method ensures the accurate representation of the program's logic and structure in the AST.

Furthermore, the parse_assignment method proves invaluable for parsing assignment statements, handling variables, numeric values, assignment operators, and logic gates. It guarantees the correct interpretation of these statements within the AST, enhancing the overall functionality of the system.

In summary, the Parser class developed in this project provides a robust and efficient solution for processing input tokens and constructing an Abstract Syntax Tree. The adherence to established grammatical rules and the handling of unexpected tokens through SyntaxError detection demonstrate the project's commitment to accuracy and reliability. This endeavor has equipped me with valuable skills in parsing, AST construction, and error handling, which can be applied in diverse programming contexts.
