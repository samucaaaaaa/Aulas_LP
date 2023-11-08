"""
class Carro:
    # Propriedade ou atributo
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def get_marca(self):
        print("Método get_marca foi invocado")
        return self.marca
    
    def set_marca(self, marca):
        print("Método set_marca foi invocado")
        self.marca = marca

    def get_modelo(self):
        print("Método get_modelo foi invocado")
        return self.modelo
    
    def set_modelo(self, modelo):
        print("Método set_modelo foi invocado")
        self.modelo = modelo

carro = Carro("Volvo", "XC40")
print(carro.get_marca())
print(carro.get_modelo())

# carro.marca = "BMW"
# carro.modelo = "X1"

# print(carro.marca)
# print(carro.modelo)

carro.set_marca("BMW")
carro.set_modelo("X1")

print(carro.get_marca())
print(carro.get_modelo())
"""
"""
class Carro:
    # Propriedade ou atributo
    def __init__(self, marca, modelo):
        # self._marca = marca
        # self._modelo = modelo
        self._marca = marca
        self._modelo = modelo
    
    @property
    def marca(self):
        print("Método get_marca foi invocado")
        return self._marca
    
    @marca.setter
    def marca(self, marca):
        print("Método set_marca foi invocado")
        self._marca = marca

    @property
    def modelo(self):
        print("Método get_modelo foi invocado")
        return self._modelo
    
    @modelo.setter
    def modelo(self, modelo):
        print("Método set_modelo foi invocado")
        self._modelo = modelo

    @property
    def descricao(self):
        return f"{self.marca}: {self.modelo}"


carro = Carro("Volvo", "XC40")
print(carro.marca)# Sem parênteses por conta do @property
print(carro.modelo)

carro.marca = "BMW"
carro.modelo = "X1"

print(carro.marca)
print(carro.modelo)

print(carro.descricao)
"""

class Foo:
    def __init__(self):
        self.public = "Public" # Qualquer unidade pode utilizar
        self._proctected = "Proctected" # utilizado na classe e em suas subclasses
        self.__private = "Private" # 

    def public_method(self):
        print("Método público")

    def _protected_method(self):
        print("Método protegido") 

    

    ...

class Bar(Foo):
    ...

object_ = Foo()
print(object_.public)

print("#"*40)
print("ERRO SEMÂNTICO")
print(object_._proctected)
object_._protected_method()