# Assunto novo

# 1° Parte

'''
class SerieTV:
    def __init__(self, num_temporadas, num_episodios):
        self.num_episodios = num_episodios
        self.num_temporadas = num_temporadas
        
    # Fallback repr    
    def __str__(self):
        return f"{self.num_temporadas} temporadas de {self.num_episodios} episódios"
    
    def __repr__(self):
        # class_ = type(self).__name__ Pode ser escrito assim
        class_ = self.__class__.__name__ # Assim é melhor
        
        return f"{class_}(num_temporadas={self.num_temporadas!r}, num_episodios={self.num_episodios!r})"
    
    
serie_1 = SerieTV(7, 13)      
serie_2 = SerieTV(42, 666)

print(serie_1)
print(f"{serie_1!s}")
print(repr(serie_1))

print(serie_2)
print(f"{serie_2!r}")
print(repr(serie_2))  
'''

# 2° Parte

class Aluno:
    def __init__(self, qi, nr_artigos_publicados):
        self.qi = qi
        self.nr_artigos_publicados = nr_artigos_publicados
        
    def __str__(self):
        return f"QI: {self.qi} e Publicações: {self.nr_artigos_publicados}"
    
    def __add__(self, other):
        qi_total = self.qi + other.qi
        publicacoes_acumuladas = self.nr_artigos_publicados + other.nr_artigos_publicados
        
        return Aluno(qi_total, publicacoes_acumuladas)
    
    def __gt__(self, other): #greater then
        if self.qi > other.qi:
            return True
        elif self.qi == other.qi:
            return self.nr_artigos_publicados > other.nr_artigos_publicados
        else:
            return False
        
    
aluno_1 = Aluno(100, 0)
aluno_2 = Aluno(130, 2)

#não pode fazer isso antes de criar o método __add__
super_aluno = aluno_1 + aluno_2 

print(aluno_1)
print(aluno_2)    
print(super_aluno)

#não pode fazer isso sem o método __gt__
if aluno_1 > aluno_2:
    print("O aluno 1 é MELHOR que o aluno 2")
else:
    print("O aluno 2 é MELHOR que o aluno 1")      
