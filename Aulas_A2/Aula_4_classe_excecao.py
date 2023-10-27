# Criando uma classe de exceção
class DeuRuimError(ZeroDivisionError):
    def __init__(self, message="Deu Ruim, mané!"):
        self.message = message
        super().__init__(self.message)

'''        
# Testando a exceção    
def teste():
    raise DeuRuimError()
        
try:
    teste()
except DeuRuimError:
    print("Pelo menos tentamos...")
except ZeroDivisionError:
    print("Pelo menos tentamos...")    
'''    

