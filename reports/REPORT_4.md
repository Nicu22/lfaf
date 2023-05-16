
# CNF (Chomsky Normal Form)
### Course: Formal Languages & Finite Automata
### Author: Popescu Nichifor FAF-212
### Variant: 22
## Objectives
1.  Learn about Chomsky Normal Form (CNF) [1].
2.  Get familiar with the approaches of normalizing a grammar.
3.  Implement a method for normalizing an input grammar by the rules of CNF.
    3.1.  The implementation needs to be encapsulated in a method with an appropriate signature (also ideally in an appropriate class/type).
    3.2.  The implemented functionality needs executed and tested.
    3.3.  A BONUS point will be given for the student who will have unit tests that validate the functionality of the project.
    3.4.  Also, another BONUS point would be given if the student will make the aforementioned function to accept any grammar, not only the one from the student's variant.

## Screenshots
![Rezults](/images/img3.png "Rezults")

## Implementation description
A Python dictionary, the type of data that will be mainly used, the grammar looks like this:
```
#Defining a dictionary representing a context-free grammar
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
```
Unit tests will be implemented for each of the methods responsible for each step in the CNF conversion. For unit tests, the 'unittest' module in python will be used.


The Grammar class type object is created to intake the grammar.
Additionally, a new method in the  **Grammar**  class that using this given grammar, returns a new type of object

Method RemoveEpsilon which removes epsilon productions from a grammar.

```
The method takes in a grammar object, which is assumed to be a dictionary with non-terminal 
    symbols as keys and lists of production rules as values. The method first identifies all 
    non-terminals that produce epsilon by iterating over the productions and checking if they contain 
    an empty string. It then generates all possible combinations of non-terminals that can produce epsilon 
    by iterating over the set of epsilon-producing non-terminals and creating new combinations by 
    appending each non-terminal to existing combinations. 
Next, it generates new productions to replace the epsilon-producing non-terminals by iterating over each 
    production and each combination and removing the combination from the production. 
It then updates the grammar with the new productions  by iterating over each non-terminal and 
    appending the new productions to its list of production rules. 
If the empty string is in a non-terminal's list of production rules, it removes it. Finally, it 
    removes any non-terminals that only produce epsilon and updates the non-terminal list accordingly. 
The method returns the updated grammar.
```
The new aforementioned class is basically a CNF converter, containing the methods necessary for each of the CNF conversion steps. These methods are called in the code above.

### Removing epsilon-transitions:
``` py
def  RemoveEpsilon(self):
# Step 1: Identify all non-terminals that produce ε.
# Create an empty set to store non-terminal symbols that produce epsilon (empty string)
eps_producing  =  set()
# Iterate over the keys (non-terminal symbols) and values (productions) of self.p dictionary
for  nt, prods  in  self.p.items():
# Check if the empty string is in the set of productions for the current non-terminal symbol
if  ""  in  prods:
# If so, add the current non-terminal symbol to the set of epsilon-producing symbols
eps_producing.add(nt)
# Step 2: Generate all possible combinations of non-terminals that can produce ε.
# Define an empty list to hold the epsilon combinations
eps_combinations  = [[]]
# Loop through each non-terminal symbol that produces epsilon
for  nt  in  eps_producing:
# Loop through each existing combination of epsilon-producing non-terminals
for  i  in  range(len(eps_combinations)):
# Append the current non-terminal to the existing combination and add it to the list of combinations
eps_combinations.append(eps_combinations[i] + [nt])
# Step 3: Generate new productions to replace non-terminals that produce ε.
# This code is used to remove empty productions from the grammar productions.
# A new dictionary `new_productions` is initialized to store the modified productions.
new_productions  = {}
# The for loop iterates over the grammar productions `self.p`.
# `nt` represents the non-terminal in the production and `prods` represents its corresponding productions.
for  nt, prods  in  self.p.items():
# A new empty list is created for each non-terminal.
new_productions[nt] = []
# The nested for loop iterates over the individual productions of each non-terminal.
for  prod  in  prods:
# The `eps_combinations` is a list of empty productions.
# The following code replaces each empty production in the individual production with an empty string.
# A new production is created and stored in `new_prod`.
# The loop runs for each empty production in `eps_combinations`.
for  combination  in  eps_combinations:
new_prod  =  prod
for  c  in  combination:
new_prod  =  new_prod.replace(c, "")
# The new production is appended to the list of new productions for the current non-terminal
# only if it is not already present in the list of new productions.
if  new_prod  !=  prod  and  new_prod  not  in  new_productions[nt]:
new_productions[nt].append(new_prod) 
# Step 4: Update the grammar with the new productions.
# The following code loops over a dictionary of new productions, where each key represents a non-terminal symbol
# and its value is a list of productions that can be generated by that symbol.
for  nt, prods  in  new_productions.items():
# For each production in the list, check if it's not an empty string and not already in the list of productions
# associated with the non-terminal symbol. If it satisfies both conditions, append the production to the list.
for  prod  in  prods:
if  prod  !=  ""  and  prod  not  in  self.p[nt]:
self.p[nt].append(prod)
# Check if there is an empty production in the list of productions associated with the non-terminal symbol.
# If so, remove it from the list.
if  ""  in  self.p[nt]:
self.p[nt].remove("")
# Step 5: Remove the element if it consisted only of an epsilon transition
for  key  in  self.p:
if  self.p[key] == []:
for  key1  in  self.p:
for  state  in  self.p[key1]:
if  key  in  state:
self.p[key1].remove(state)
to_be_popped.append(key)
# Remove it from dictionary and from nonterminals lists
# The following code removes the keys in the 'to_be_popped' list from the dictionary 'self.p' and also removes them from the list 'self.Vn'. Finally, it returns the modified dictionary 'self.p'.
for  key  in to_be_popped:
self.p.pop(key)
self.Vn.remove(key)
return  self.p
```
## Conclusion
In conclusion, lexical analysis and scanners play a crucial role in the field of programming language processing. They are fundamental components that facilitate the translation of human-readable code into machine-readable tokens, enabling effective compilation and interpretation of programming languages.
Throughout this report, we have explored the key concepts and techniques involved in lexical analysis and scanners. We have discussed how lexical analysis breaks down source code into tokens, which are subsequently used by parser's to construct meaningful syntax trees. Additionally, we have examined the role of scanners in recognizing and categorizing lexical elements, such as identifiers, keywords, operators, and literals.
Furthermore, we have explored various scanning algorithms, including regular expressions, finite automata, and lexing tools, which are used to efficiently implement scanners. These algorithms provide the necessary flexibility, speed, and accuracy required for processing programming languages effectively.
Moreover, we have highlighted the importance of error handling and error recovery in lexical analysis. Robust error handling mechanisms allow for graceful handling of lexical errors, providing meaningful error messages to developers and aiding in the debugging process.
Lexical analysis and scanners are not only crucial in the compilation process but also in other areas such as code editors, code refactoring tools, and syntax highlighting. Their accurate and efficient functioning significantly impacts the overall development experience and productivity of programmers.
As programming languages continue to evolve and new languages emerge, the techniques and tools used in lexical analysis and scanners will continue to evolve as well. Advancements in language design, scanning algorithms, and automation tools will further enhance the capabilities of lexical analysis and scanners, enabling more efficient and reliable processing of programming languages.
In conclusion, lexical analysis and scanners are foundational components in programming language processing, enabling the translation of human-readable code into machine-executable instructions. Their effective implementation is vital for creating efficient compilers, interpreters, and other tools that facilitate software development.
