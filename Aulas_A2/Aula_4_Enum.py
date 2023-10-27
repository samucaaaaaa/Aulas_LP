# O Enum atribui uma constante (um valor) as coisas
from enum import Enum

class Escolas(Enum):
    EMAp = 1
    EBAPE = 2
    DIREITO_RIO = 3
    
class Meses(Enum):
    JANEIRO = 1
    FEVEREIRO = 2
    MARCO = 3
    
print(Escolas.EMAp)  
print(Escolas.EMAp.name) 
print(Escolas.EMAp.value)         
  
print(type(Escolas.EMAp))  
print(type(Escolas.EMAp.name)) 
print(type(Escolas.EMAp.value))    

# Será False, pois EMAp tem valor 1 e EBAPE tem valor 2
print(Escolas.EMAp == Escolas.EBAPE)

# Será True, pois o valor de FEVEREIRO é maior do que o valor de JANEIRO
print(Meses.FEVEREIRO.value > Meses.JANEIRO.value)
