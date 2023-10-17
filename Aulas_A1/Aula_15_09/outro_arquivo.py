import unittest
import teste_unitario as ut

'''
# Teste Automatizado x Teste Manual
# Automatizado: feito pelo programador; Manual: Alguém usa o sistema para testá-lo 

# Teste Exploratório
print(ut.fatorial(7))
print(ut.fatorial(5))
print(ut.fatorial(0))
print(ut.fatorial(42))
print(ut.fatorial(5.0))
'''

# A classe TestFatorial é filha da classe TesteCase do módulo unittest
class TestFatorial(unittest.TestCase):
    #Equivalence Partitioning Method
    #Equivalence Class Partitioning (ECP)
    def teste_maior_que_1(self):
        #self.assertEqual(ut.fatorial(2),2)
        #self.assertEqual(ut.fatorial(3),6)
        #self.assertEqual(ut.fatorial(4),24)
        self.assertEqual(ut.fatorial(5),120)
        
    def teste_menor_que_0(self):
        self.assertEqual(ut.fatorial(-7),1)      
        
    #Boundary value Analysis ou Boundary value test
    def teste_igual_1(self):
        self.assertEqual(ut.fatorial(1),1)
        
    def teste_igual_0(self):
        self.assertEqual(ut.fatorial(0),1)  
        
    # Data type Checking
    def teste_tipo_dado(self):
        self.assertRaises(TypeError, ut.fatorial, "Oi")
        self.assertEqual(ut.fatorial(2.0),2.0)
        
        
# Quando alguém rodar esse arquivo como "main", rode todos os testes:
if __name__ == "__main__":
    unitest.main()