
# Intro to formal languages. Regular grammars. Finite Automata.
### Course: Formal Languages & Finite Automata
### Author: Popescu Nichifor FAF-212
### Variant: 22
## Theory
Def: 
Lexical Analysis and Scanners: for the purposes of this laboratory, lexical analysis means the transformation of a sequence of characters into a series of lexical tokens. The program/algorithm that does this is called the lexer (or scanner), and it is the main character of this here laboratory.

## Screenshots
![Rezults](/images/img2.png "Rezults")

## Implementation description

The class new 'Lexer' was created, that opens a text file where the code in the given language is.


The particular code that will be used, looks like this:
**Variant 22**
```
BEGIN
v
INPUT
I 011. Q 011;
OUTPUT
Q 011. M 011;
RAM
CN01.AND I 011. Q 011 . CN04.NOT Q 011. I 011;
I 011 := NOT I 011
END
```
How the algorithm works, is by mapping the grammar into a dictionary:
```
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
```
From the code file, the algorithm separates the code into individual words, by use of the '.split()' method, and splits them again if there are any points or semicolons.

From there on, using the dictionary, the words are tokenized, according to their keyes. If the word is numeric, it also tokenized, despite not being in the dictionary.

If, however, the word is not in the grammar or a numeric one, it is defined as 'unknown'.

The end result, i.e. the token list, for the provided code looks like this:
```
[['keywords', 'BEGIN'], ['unknown', 'v'], ['keywords', 'INPUT'], 
['variables', 'I'], ['numeric', '011'], ['separators', '.'], 
['variables', 'Q'], ['numeric', '011'], ['separators', ';'], 
['keywords', 'OUTPUT'], ['variables', 'Q'], ['numeric', '011'],
['separators', '.'], ['variables', 'M'], ['numeric', '011'], 
['separators', ';'], ['keywords', 'RAM'], ['contacts', 'CN01'], 
['separators', '.'], ['logic gates', 'AND'], ['variables', 'I'], 
['numeric', '011'], ['separators', '.'], ['variables', 'Q'], 
['numeric', '011'], ['separators', '.'], ['contacts', 'CN04'], 
['separators', '.'], ['logic gates', 'NOT'], ['variables', 'Q'], 
['numeric', '011'], ['separators', '.'], ['variables', 'I'], 
['numeric', '011'], ['separators', ';'], ['variables', 'I'], 
['numeric', '011'], ['operators', ':='], ['logic gates', 'NOT'], 
['variables', 'I'], ['numeric', '011'], ['keywords', 'END']]

```
## Conclusion
In conclusion, lexical analysis and scanners play a crucial role in the field of programming language processing. They are fundamental components that facilitate the translation of human-readable code into machine-readable tokens, enabling effective compilation and interpretation of programming languages.
Throughout this report, we have explored the key concepts and techniques involved in lexical analysis and scanners. We have discussed how lexical analysis breaks down source code into tokens, which are subsequently used by parser's to construct meaningful syntax trees. Additionally, we have examined the role of scanners in recognizing and categorizing lexical elements, such as identifiers, keywords, operators, and literals.
Furthermore, we have explored various scanning algorithms, including regular expressions, finite automata, and lexing tools, which are used to efficiently implement scanners. These algorithms provide the necessary flexibility, speed, and accuracy required for processing programming languages effectively.
Moreover, we have highlighted the importance of error handling and error recovery in lexical analysis. Robust error handling mechanisms allow for graceful handling of lexical errors, providing meaningful error messages to developers and aiding in the debugging process.
Lexical analysis and scanners are not only crucial in the compilation process but also in other areas such as code editors, code refactoring tools, and syntax highlighting. Their accurate and efficient functioning significantly impacts the overall development experience and productivity of programmers.
As programming languages continue to evolve and new languages emerge, the techniques and tools used in lexical analysis and scanners will continue to evolve as well. Advancements in language design, scanning algorithms, and automation tools will further enhance the capabilities of lexical analysis and scanners, enabling more efficient and reliable processing of programming languages.
In conclusion, lexical analysis and scanners are foundational components in programming language processing, enabling the translation of human-readable code into machine-executable instructions. Their effective implementation is vital for creating efficient compilers, interpreters, and other tools that facilitate software development.
