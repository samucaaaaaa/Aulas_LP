
'''
# As classes vão criar novos tipos dentro do python
class Classe:
    def __init__(self): # método construtor
        pass

def func():
    pass

print(type(Classe))
print(type(func))
print(dir(int()))
print(dir(Classe))
'''
# Algumas funcionalidades: os métodos vão ser exclusivos de determinados tipos (classes)
class Point2D(object): # onde colocamos os parâmetros em funções, vamos colocar a classe mãe
    def __init__(self, x, y) -> None: # os métodos de uma classe são os comportamentos daquela classe
        # método de inicialização, ele é necessário para que todo objeto seja criado
        self.x = x # as propriedades dentro do método __init__ vão estar presentes em todos os objetos dessa classe
        self.y = y
    
    # Métodos setters, eles vão configurar atributos
    def set_x(self, novo_x):
        self.x = novo_x
    
    def set_y(self, novo_y):
        if novo_y == self.y:
            print("O valor é igual ao anterior. Nada foi alterado!") # podemos adotar algumas estratégias para evitar que o usuário altere alguns atributos da classe
        else:
            self.y = novo_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
    
ponto = Point2D(5, 6)
print(type(ponto))

print(ponto.x)

ponto.set_x(10)
print(ponto.x)

print(ponto.y)

# Testando a regra de negócio criada
ponto.set_y(6)

# Vai fazer a mesma coisa do set_y, mas não é recomendado, mas no python não podemos proibir
ponto.y = 20

print(ponto.get_x())
print(ponto.get_y())