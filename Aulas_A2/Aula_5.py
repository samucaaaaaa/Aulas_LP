class Fruta:
    def __init__(self, nome):
        self.nome = nome

    def comer(self):
        print(f"A fruta {self.nome} está sendo comida...")

banana = Fruta("Banana")
banana.comer()
Fruta.comer(banana)

uva = Fruta("Uva")
print(vars(uva))
print(uva.__dict__)

uva.peso = 1
uva.data = "31/10/2023"
print(uva.__dict__)

del uva.__dict__["peso"]
del uva.__dict__["data"]
# del uva.__dict__["nome"]

# print(uva.__dict__)

uva.__dict__["tipo"] = "roxa"

print(uva.__dict__)

class Produto:
    data_atual = 11 #Mês atual

    def __init__(self, fabricacao):
        self.fabricacao = fabricacao
    
    def tempo_de_prateleira(self):
        return Produto.data_atual - self.fabricacao
    
produto_1 = Produto(8)
produto_2 = Produto(10)

print(Produto.data_atual)
print(produto_1.tempo_de_prateleira())
print(produto_2.tempo_de_prateleira())