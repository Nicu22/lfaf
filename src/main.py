from lexer import Lexer
from parser_1 import Parser


if __name__ == "__main__":
    code = '''
    Description {
        name="Casimir"
        type="NPC"
        mbti="intj"
        role="protagonist"
        background="Casimir was a farmer before turning mercenary."
    }
    Setting {
        type="game" 
        category="strategy, fantasy, medieval"
        background="3 knights are in a fantasy land"
    }
    Response {
        length=300
        prompt="What is your background history?"
    }'''

    lexer = Lexer()
    tokens = lexer.tokenize(code)
    print(tokens)

    parser = Parser(tokens)
    trees = parser.parse()
    for tree in trees:
        print(tree)
