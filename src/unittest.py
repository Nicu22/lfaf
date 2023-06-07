import unittest
from cnf import CNFConvertor
from Grammar import RegularGrammar

vn = ['S','A','B','C','D','X']
vt = ['a','b']
p = {
'S' : ['dB','A'],
'A' : ['d','dS', 'aAdAB'],
'B' : ['aC','aS','AC'],
'C' : [''],
'E' : ['AS']
}
a = vt

correct = {
    'S' : ['d', 'DB', 'DS', 'FG'],
    'A' : ['d', 'DS', 'FG'],
    'B' : ['a', 'd', 'HS', 'DS', 'FG'],
    'D' : ['d'],
    'F' : ['HA'],
    'G' : ['DI'],
    'H' : ['a'],
    'I' : ['AB']
}

class TestMethods(unittest.TestCase):
    
    def setUp(self):
        self.cnf_grammar = CNFConvertor(p,vn)
        self.reg_grammar = RegularGrammar(vn,vt,p,a)

    def test_eps_rem(self):
        self.assertEqual(self.cnf_grammar.RemoveEpsilon(),correct,'The epsilon was not removed correctly')

    def test_unit_rem(self):
        self.assertEqual(self.reg_grammar.ConvertCNF(),correct,'The unit production removal was not correct')

    def test_unpr_rem(self):
        self.cnf_grammar.p = correct
        self.assertEqual(self.cnf_grammar.RemoveUnproductive(),correct,'The unprodoctive removal went wrong')

    def test_cln(self):
        self.cnf_grammar.p = correct
        self.assertEqual(self.cnf_grammar.Cleanup(),correct,'The cleanup went wrong!')




if __name__ == '__main__':
    unittest.main()