x = 10
y = 0 


try:
    resultado = x/y
    raise ZeroDivisionError
except NameError:
    print("Variável não existe")
except ZeroDivisionError:
    print("Não é possível realizar o divisor")          
except: 
    print("")

try:
    resultado = x / y
except NameError as erro:
    print("Variável não existe", erro.__class__)
except Exception:
    print("Não é possível realizar o divisor")  
    
try:
    resultado = 10 / y
except (ZeroDivisionError, NameError) as erro:
    print("Variável não existe", erro)
except Exception:
    print("Não é possível realizar o divisor")    