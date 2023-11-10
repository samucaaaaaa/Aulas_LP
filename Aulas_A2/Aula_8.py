print("EXEMPLO 1:\n")

class EMAp:
    def __init__(self, nr_alunos):
        self.nr_alunos = nr_alunos
        
escola = EMAp(42)
print(escola.nr_alunos)
print(escola,"\n")
escola_como_um_homem = object().__new__(EMAp)
escola_como_um_homem.__init__(666)
print(escola_como_um_homem) 
print(escola_como_um_homem.nr_alunos) 

print("\n#################################################################################################")
print("\nEXEMPLO 2:\n")

class EMAp_2:
    def __new__(cls, *args, **kwargs):
        print("Podemos fazer o que quisermos antes da instância ser criada")
        object_ = super().__new__(cls)
        print("Podemos fazer o que quisermos antes da instância ser criada")
        return object_
    
    def __init__(self, nr_alunos):
        self.nr_alunos = nr_alunos

escola = EMAp_2(42)
print("\n", escola.nr_alunos)
escola_como_um_homem = object().__new__(EMAp_2)
escola_como_um_homem.__init__(666)
print(escola_como_um_homem.nr_alunos)       

print("\n#################################################################################################")
print("\nEXEMPLO 3:\n")

from abc import ABC, abstractmethod

class Aluno(ABC):
    def __init__(self):
        self._cr = 0
        
    @abstractmethod    
    def _estudar(self, disciplina): ...    
        
    def realizar_prova(self, disciplina):
        print(f"Realizando prova de {disciplina}")
        
    @property 
    @abstractmethod
    def cr(self): ...
        
# Essa é uma classe concreta, pois ela herda da classe abstrata Aluno
class AlunoEMAp(Aluno):
    def _estudar(self, disciplina):
        print(f"Estudando - com afinco - {disciplina}")
    
    @property
    def cr(self):
        return self._cr
    
    @cr.setter 
    def cr(self, cr):
        self.cr = cr
                
    
# Não podemos executar isso, pois Aluno é uma classe abstrata (ela herda uma metaclasse e possui um método abstrato):
'''      
aluno = Aluno()
aluno.realizar_prova("Linguagens de Programação")        
'''

# Assim funciona
aluno_emap = AlunoEMAp()
aluno_emap.realizar_prova("Linguagens de Programação")  
aluno_emap._estudar("Linguagens de Programação") 
