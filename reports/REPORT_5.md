
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

### Types of tokens

`Suite`, `Test`, and `Order` are the three categories, and each has a specific function within the script.

The parsing method begins with the parse method. To go on to the next token, it calls the advance method, and to parse the complete program, it calls the parse_program method.
By using the advance method, the parser advances to the following token in the list of tokens. It makes the appropriate adjustments to the current_token_index and current_token variables.
If the current token and the anticipated token type match, the match function returns true. If so, it uses the advance function to move on to the next token. If not, a Syntax Error is raised with the proper error message.

## Implementation description
Inside the `parser_1.py` we have 2 classes: `Node` and `Parser`. The code for `Node` class is the following:
```
def  __init__(self, type, children=None, leaf=None):
	self.type  =  type
	if  children:
	self.children  =  children
	else:
	self.children  = []
	self.leaf  =  leaf
 
def  __str__(self, level=0):
	ret  =  "\t"*level+repr(self.type)
	if  self.leaf  is  not  None:
	ret  +=  " ("  +  repr(self.leaf) +  ")"
	ret  +=  "\n"
	for  child  in  self.children:
	ret  +=  child.__str__(level+1)
	return  ret
```

A node in the Abstract Syntax Tree (AST) is represented by the Node class. Each node has a leaf value, a list of children (also nodes), and a type (such as "DESCRIPTION," "NAME," "TYPE," etc.). If a node has a leaf value, that is what it actually is worth. The leaf value of a node for a "NAME," for instance, would be the name itself, such as "Casimir."

The Node class's __str__ method is used to transform a node to a string that reveals its structure. The string representations of all the child nodes are indented to illustrate their depth in the tree and include the type of the node, the leaf value (if present), and their string representations.

To parse a list of tokens and create an AST, use the Parser class. It keeps track of its position in the list using a current_token index and a list of tokens.

The Parser class's source code is as follows:
```
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = 0

    def eat(self, token_type):
        if self.tokens[self.current_token][0] == token_type:
            self.current_token += 1
        else:
            raise Exception(
                f"Unexpected token type: {self.tokens[self.current_token][0]}. Expected: {token_type}")

    def parse(self):
        nodes = []
        while self.current_token < len(self.tokens):
            if self.tokens[self.current_token][0] == 'DESCRIPTION':
                nodes.append(self.description())
            elif self.tokens[self.current_token][0] == 'SETTING':
                nodes.append(self.setting())
            elif self.tokens[self.current_token][0] == 'RESPONSE':
                nodes.append(self.response())
            else:
                raise Exception(
                    f"Unexpected token type: {self.tokens[self.current_token][0]}")
        return nodes

    def description(self):
        self.eat('DESCRIPTION')
        self.eat('LEFT_BRACE')
        name = self.name()
        type = self.type()
        mbti = self.mbti()
        role = self.role()
        background = self.background()
        self.eat('RIGHT_BRACE')
        return Node('DESCRIPTION', [name, type, mbti, role, background])

    def name(self):
        self.eat('NAME')
        self.eat('EQUALS')
        name = self.tokens[self.current_token][1]
        self.eat('STRING_LITERAL')
        return Node('NAME', [], name)

    def type(self):
        self.eat('TYPE')
        self.eat('EQUALS')
        type = self.tokens[self.current_token][1]
        self.eat('STRING_LITERAL')
        return Node('TYPE', [], type)

    def mbti(self):
        self.eat('MBTI')
        self.eat('EQUALS')
        mbti = self.tokens[self.current_token][1]
        self.eat('STRING_LITERAL')
        return Node('MBTI', [], mbti)

    def role(self):
        self.eat('ROLE')
        self.eat('EQUALS')
        role = self.tokens[self.current_token][1]
        self.eat('STRING_LITERAL')
        return Node('ROLE', [], role)

    def background(self):
        self.eat('BACKGROUND')
        self.eat('EQUALS')
        background = self.tokens[self.current_token][1]
        self.eat('STRING_LITERAL')
        return Node('BACKGROUND', [], background)

    def setting(self):
        self.eat('SETTING')
        self.eat('LEFT_BRACE')
        type = self.type()
        category = self.category()
        background = self.background()
        self.eat('RIGHT_BRACE')
        return Node('SETTING', [type, category, background])

    def category(self):
        self.eat('CATEGORY')
        self.eat('EQUALS')
        category = self.tokens[self.current_token][1]
        self.eat('STRING_LITERAL')
        return Node('CATEGORY', [], category)

    def response(self):
        self.eat('RESPONSE')
        self.eat('LEFT_BRACE')
        length = self.length()
        prompt = self.prompt()
        self.eat('RIGHT_BRACE')
        return Node('RESPONSE', [length, prompt])

    def length(self):
        self.eat('LENGTH')
        self.eat('EQUALS')
        length = self.tokens[self.current_token][1]
        self.eat('NUMBER_LITERAL')
        return Node('LENGTH', [], length)

    def prompt(self):
        self.eat('PROMPT')
        self.eat('EQUALS')
        prompt = self.tokens[self.current_token][1]
        self.eat('STRING_LITERAL')
        return Node('PROMPT', [], prompt)
```
A specific sort of token is consumed using the eat method. The current_token index is moved to the following token if the current token has the expected type. If not, an exception is raised.

The primary method that initiates the parsing process is the parse method. Until all of the tokens have been eaten, it keeps consuming tokens and constructing nodes.

The 'DESCRIPTION', 'SETTING', and 'RESPONSE' blocks are parsed using the relevant description, setting, and response methods. For each of these methods, a new node of the proper kind is created, the block's tokens are consumed, and further nodes are added for each component.

The  `name`,  `type`,  `mbti`,  `role`,  `background`,  `category`,  `length`, and  `prompt`  methods are used to parse the individual parts of a block. Each of these methods creates a new node of the appropriate type, consumes the tokens that make up the part, and sets the leaf value of the node to the actual value from the tokens.

The  `Parser`  class outputs such a result, in the form of an AST:

```
'DESCRIPTION'
        'NAME' ('Casimir')
        'TYPE' ('NPC')
        'MBTI' ('intj')
        'ROLE' ('protagonist')
        'BACKGROUND' ('Casimir was a farmer who became a mercenary')

'SETTING'
        'TYPE' ('game')
        'CATEGORY' ('medieval, fantasy, horror')
        'BACKGROUND' ('A fantasy land where there are 3 knights')

'RESPONSE'
        'LENGTH' (300)
        'PROMPT' ('What is your background history?')
``` 

## Conclusion

In this laboratory work, we made significant progress in developing a project aimed at compiling a sample code for a programming language. Building upon the previous step of lexical analysis, we focused on implementing a parser to conduct syntax analysis. The parser played a crucial role in processing the tokens generated by the lexer and organizing them in a structured manner that reflects their syntactic relationships.

The development of the parser drew upon the knowledge and experience gained from working on the Problem-Based Learning (PBL) project. While the approach used for the parser in this laboratory work differed from the one employed in the PBL project, the fundamental concepts and principles remained applicable. This cross-application of knowledge allowed for a deeper understanding of parsing techniques and their adaptation to different scenarios.

By successfully implementing the parser, we achieved an essential milestone in the overall project of creating a compiler. The parser's role in analyzing the syntax of the code is instrumental in identifying and validating its correctness based on the language's grammar rules. This step brings us closer to the ultimate goal of transforming source code into executable programs.

As the project progresses, we will continue to refine and expand upon the parser's capabilities, integrating it further into the broader compilation process. The knowledge and experience gained from working on this parser will serve as a foundation for tackling future challenges in compiler development and deepening our understanding of language parsing techniques.
