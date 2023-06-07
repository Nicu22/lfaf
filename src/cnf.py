import itertools

class CNFConvertor:
    def __init__(self, p, Vn):
        self.p = p   
        self.Vn = Vn 
        self.unavailable_tokens = [ord(x) for x in self.Vn]

    def RemoveEpsilon(self):

        eps_producing = set()
        for nt, prods in self.p.items():
            if "" in prods:
                eps_producing.add(nt)

        eps_combinations = [[]]
        for nt in eps_producing:
            for i in range(len(eps_combinations)):
                eps_combinations.append(eps_combinations[i] + [nt])

        new_productions = {}
        for nt, prods in self.p.items():
            new_productions[nt] = []
            for prod in prods:
                for combination in eps_combinations:
                    new_prod = prod
                    for c in combination:
                        new_prod = new_prod.replace(c, "")
                    if new_prod != prod and new_prod not in new_productions[nt]:
                        new_productions[nt].append(new_prod)

        for nt, prods in new_productions.items():
            for prod in prods:
                if prod != "" and prod not in self.p[nt]:
                    self.p[nt].append(prod)
            if "" in self.p[nt]:
                self.p[nt].remove("")

        to_be_popped = []
        for key in self.p:
            if self.p[key] == []:
                for key1 in self.p:
                    for state in self.p[key1]:
                        if key in state:
                            self.p[key1].remove(state)

                to_be_popped.append(key)

        for key in to_be_popped:
            self.p.pop(key)
            self.Vn.remove(key)

        return self.p

   
    def RemoveCycles(self):

        for key in self.p:
            for state in self.p[key]:
                if len(state) == 1 and state.isupper():

                    for state1 in self.p[state]:
                        if state1 == key:

                            for state2 in self.p[state]:
                                if state2 != key:
                                    self.p[key].append(state2)

                            self.p[state] = []
                            break

 
    def RemoveUnitProd(self,key):

        for state in self.p[key]:
            self.RemoveCycles()
            if len(state) == 1 and state.isupper():
                for state1 in self.p[state]:
                    if len(state1) == 1 and state1.isupper():
                        self.RemoveUnitProd(state)

                    self.p[key].append(state1)
                self.p[key].remove(state)


    def RemoveUnproductive(self):

        to_be_popped = []

        for key in self.p:
            terminals = 0
            for state in self.p[key]:
                if state.islower():
                    terminals += 1

            if terminals == 0:
                to_be_popped.append(key)

        for key in to_be_popped:
            self.p.pop(key)
            self.Vn.remove(key)

        return self.p

    def Cleanup(self):

        for key in self.p:
            for state in self.p[key]:
                for letter in state:
                    if letter.isupper() and letter not in self.Vn:
                        self.p[key].remove(state)

        for nont in self.Vn:
            encounters = 0
            for key in self.p:
                if key != nont:
                    for state in self.p[key]:
                        if nont in state:
                            encounters += 1

            if encounters == 0:
                if nont in self.p:
                    self.p.pop(nont)
                self.Vn.remove(nont)

        return self.p

    def Modifiable(self,state):

        if len(state) == 1 and state.islower():
            return False

        if len(state) == 2 and state.isupper():
            return False

        return True

 
    def Transform(self):

        new_dict = {}
        changes = True
        available_tokens = [x for x in range(65, 91) if x not in self.unavailable_tokens]
        while changes:
            changes = False

            for key in self.p:
                for state in self.p[key]:
                    if self.Modifiable(state):
                        new_state = ''
                        if len(state[0:len(state)//2]) == 1 and state[0:len(state)//2].isupper():
                            new_state += state[0:len(state)//2]
                        elif state[0:len(state)//2] in new_dict:
                            new_state += new_dict[state[0:len(state)//2]]
                        else:
                            xnode1 = chr(available_tokens[0])
                            available_tokens.pop(0)

                            new_state += xnode1
                            self.Vn.append(xnode1)
                            self.p[xnode1] = []
                            self.p[xnode1].append(state[0:len(state)//2])
                            new_dict[state[0:len(state)//2]] = xnode1

                        if len(state[len(state)//2:]) == 1 and state[len(state)//2:].isupper():
                            new_state += state[len(state)//2:]
                        elif state[len(state)//2:] in new_dict:
                            new_state += new_dict[state[len(state)//2:]]
                        else:
                            xnode2 = chr(available_tokens[0])
                            available_tokens.pop(0)

                            new_state += xnode2
                            self.Vn.append(xnode2)
                            self.p[xnode2] = []
                            self.p[xnode2].append(state[len(state)//2:])
                            new_dict[state[len(state)//2:]] = xnode2

                        self.p[key].remove(state)
                        self.p[key].append(new_state)

                        changes = True
                        break
                if changes:
                    break

            for key in self.p:
                self.p[key] = list(dict.fromkeys(self.p[key]))
