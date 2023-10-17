"""Documentação do módulo

Bçá-blá-blá

"""

# Função que calcula montante e juros em um regime de juros simples
# Type Hint: MyPy
def juros_simples(capital: int, taxa: float, tempo: int) -> tuple:
    juros  = capital * (taxa/100) * tempo
    montante = capital + juros
    
    # TODO: Alterar estrutura de dados de retorno para lista
    # TODO: Limitar montante e capital a dois dígitos decimais
    return (montante, juros)

def juros_compostos(capital, taxa, tempo):
    montante = capital * (pow(1 + taxa / 100), tempo)
    juros = montante - capital
    
    return(round(montante,2), round(juros,2))