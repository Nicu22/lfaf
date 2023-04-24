~~# **Regular Grammars. Finite Automata**
### Course: Formal Languages & Finite Automata
### Author: Popescu Nichifor FAF-212
## Theory
Def:
**Language** - a means of communicating information, by using visual or audio interpretations of words.
**Formal language** - a set of strings based on an alphabet that are generated with the help of a grammar.
**String** - a combination of symbols generated with the help of rules from the production set.
**Grammar** - an entity defined by four elements: the set of non-terminal symbols, the set of terminal symbols, the start symbol, and the set of production rules.
**Automation** - an abstract computational device. It contains the states, an alphabet, transition functions for each state, the initial and final states.
**Finite automaton** - an automaton with finite amounts of states and transitions.
## **Objectives**
Understand what a language is and what it needs to have in order to be considered a formal one.
Provide the initial setup for the evolving project that you will work on during this semester. I said project because usually at lab works, I encourage/impose students to treat all the labs like stages of development of a whole project. Basically you need to do the following:
-   Create a local && remote repository of a VCS hosting service (let us all use Github to avoid unnecessary headaches);
-   Choose a programming language, and my suggestion would be to choose one that supports all the main paradigms;
-   Create a separate folder where you will be keeping the report. This semester I wish I won't see reports alongside source code files, fingers crossed;
According to your variant number (by universal convention it is register ID), get the grammar definition and do the following tasks:
-   Implement a type/class for your grammar;
-   Add one function that would generate 5 valid strings from the language expressed by your given grammar;
-   Implement some functionality that would convert and object of type Grammar to one of type Finite Automaton;
-   For the Finite Automaton, please add a method that checks if an input string can be obtained via the state transition from it;
## Implementation description
The grammar was implemented under this format. Vn and Vt represent the non-terminal and terminal set of characters respectively. The transition set P contains a list of pairs. A pair consists of two strings where the first string shows what combination of terminal and non-terminal characters should convert into the second string. The first non-terminal character in the set is used as the starting character, whereas by convention, the starting character is 'S'.
```
Vn = ['S', 'B', 'D', 'Q']
Vt = ['a', 'b', 'c', 'd']
P = [
    ['S', 'aB'],
    ['S', 'bB'],
    ['B', 'cD'],
    ['D', 'dQ'],
    ['Q', 'bB'],
    ['D', 'a'],
    ['Q', 'dQ']
]
```
The FA was implemented under this format. Q is the set of all states, Sigma is the alphabet, q0 is the initial state and F is the set of final states possible. Delta is the transition set, it contains lists of 3 strings. The first string is the state the FA is in, the second string is the character the FA is checking, and the third string is the state the FA will transition to.
```
Q = ['S', 'B', 'D', 'Q', 'Final']
Sigma = ['a', 'b', 'c', 'd']
Delta = [
['S', 'a', 'B']
['S', 'b', 'B']
['B', 'c', 'D']
['D', 'd', 'Q']
['Q', 'b', 'B']
['D', 'a', 'Final']
['Q', 'd', 'Q']
]
q0 = 'S'
F = 'Final'
```
In the method below, using a while loop, I'm replacing the non-terminals with their respective strings until there are no more non-terminal characters. The replaced strings are chosen randomly given there are multiple ways for a non-terminal to transition.
```
while switch:
    switch = 0
    for char in self.non_terminal_chars:
        if char in iterated_string:
            choice_index = choice(index_return(self.transition_set,char))
            iterated_string = iterated_string.replace(char, self.transition_set[choice_index][1])
            switch = 1
```
The index_return function iterates through the transition set and adds all the indices where the passed non-terminal is present.
```
for i in range(len(list)):
    if list[i][0] == a:
    temp.append(i)
```
In order to convert the grammar to a finite automaton, I implemented a Convertor class with the respective method. By using a for loop, I iterated through the transition set of the grammar, extracting the necessary non-terminal and terminal characters for the finite automaton. However, there is a special case where the result string from the transition set is only a character long, that is when there no any non-terminal characters in string, meaning we should use a unconventionally chosen 'Final' state for the FA.
```
for non_terminal, result in grammar.transition_set:
    if len(result) > 1:
        delta_function.append([non_terminal, result[0], result[1:]])
    else:
        delta_function.append([non_terminal, result[0], 'Final'])
```
For the construction of the FA, we use the non-terminal characters and the 'Final' state as the set of all states in the FA. The alphabet of the grammar is used for the set of terminal characters. The initial state is chosen as the first non-terminal character of the Grammar.
```
FiniteAutomaton(
    grammar.non_terminal_chars + ['Final'],
    grammar.terminal_chars,
    delta_function,
    grammar.non_terminal_chars[0],
    'Final'
)
```
The method below, by using a for loop, I iterated through each character of the passed string. I then identified the index of each state/character pair in the delta function, if the pair is not contained in the delta function, then the function returns -1, which by an if statement, will return False. The current state is changed to the respective state from the delta function. The process is repeated until the end of the string, where it will be checked whether the current state is a final state. Note that this method won't work in case the FA is non-deterministic.
```
current_state = self.initial_state
for char in string:
    a = index_return(current_state, char, self.delta_function)
    if a == -1:
        return False
    current_state = self.delta_function[a][2]
if current_state == self.final_states:  
    return True
return False
```
The index_return function here is different than the previous one, though it functions in a similar way. It looks for the matching state/character pair in the passed delta function.
```
for i in range(len(list)):
    if a == list[i][0] and b == list[i][1]:
        return i
return -1
```
## Results
The following strings are generated by my grammar given the variant. The FA immediately checks if they belong to the language.
```
Generated strings:
bcdbca
The string belongs to the finite automata
acddbca
The string belongs to the finite automata
acdbca
The string belongs to the finite automata
aca
The string belongs to the finite automata
bca
The string belongs to the finite automata
```
If instead I input "stranger" strings into the finite automaton, it will return the following message.
```
Stranger strings:
abc
The string does not belong to the finite automata
efg
The string does not belong to the finite automata
adadada
The string does not belong to the finite automata
bbbb
The string does not belong to the finite automata
adddddaaa
The string does not belong to the finite automata
```
## Conclusion
In conclusion, we have implemented a Python program that generates valid strings for a given context-free grammar and converts the grammar to a finite automaton. The program includes several classes, methods, and unit tests to ensure correct functionality. Overall, this program provides a useful tool for generating valid strings for a given context-free grammar and checking if they are accepted by a finite automaton, which has a wide range of applications in various fields, such as natural language processing, programming languages, and computer science.~~
