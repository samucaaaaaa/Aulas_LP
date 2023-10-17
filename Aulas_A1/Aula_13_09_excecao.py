#Aula

x = 10
y = 0

try:
    resultado = x/y 
    print(resultado)
    
except (NameError, ZeroDivisionError) as erro:
    print("Errou Feio! Erro: ", type(erro), erro.__class__.mro())    
else:
    print("Se der tudo certo cai aqui")
finally:
    print("Foi uma honra estudar ao seu lado.")
    
peso = -1

if peso < 0:
    raise ValueError("Peso deve ser positivo")    