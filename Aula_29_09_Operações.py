import pandas as pd
import numpy as np

print("#### Criando DATAFRAMES ####")

indices = ["The Pacific", "Black Mirror", "CSI", "NCIS", "Lost"]
colunas = ["Notas", "Temporadas", "Episódios"]
dados = [[8.3, 1, 10], [8.7, 6, 27], [7.7, 15, 337], [6.9, 14, 458], [8.3, 6, 121]]
df = pd.DataFrame(dados, index=indices, columns=colunas)
print(df, end="\n\n")

print("\n\n\n######## MULTI-INDEX ########")

plataforma = ["HBO", "HBO", "Netflix", "Netflix"]
lancamento = [2020, 2021, 2020, 2021]
indices = pd.MultiIndex.from_arrays([plataforma, lancamento], names=("Plataforma", "Lançamento"))
print("\n\nIndices: ")
print(indices)

print("\nSem Índice: ")
df.reset_index(inplace=True)
print(df)

print("\nRenomear Índice: ")
df.rename(columns={"index": "Nome"}, inplace=True)
print(df)

print("\nConfigurar Índice: ")
df.set_index(indices, inplace=True)
print(df)

print("\nSeleção Multi-Index 1: ")
print(df.loc["HBO"])

print("\nSeleção Multi-Index 2: ")
print(df.loc["HBO"].loc[2021])

print("\nSeleção Multi-Index 3: ")
print(df.xs("HBO"))

print("\nSeleção Multi-Index 3: ")
print(df.xs("HBO", 2020))

print("\nCross Selection: ")
print(df.xs(2020, level="Lançamento"))


print("\n\n######## OPERAÇÕES ########")

print(df.head())
print(df.tail())

print("Unique", df["Notas"].unique()) #Elementos únicos
print("Nunique", df["Notas"].nunique()) #Número de elementos únicos
print("Count", df["Notas"].count()) #Contagem
print("Value Counts", df["Nota"].value_counts()) #Contagem de valores

df.at[("HBO", 2020), "Nota"] = 8.7

print("Unique", df["Notas"].unique()) #Elementos únicos
print("Nunique", df["Notas"].nunique()) #Número de elementos únicos
print("Count", df["Notas"].count()) #Contagem
print("Value Counts", df["Nota"].value_counts()) #Contagem de valores

print("\n\n\n###### OPERÇÕES AGREGADAS ######")

print("Min: ", df["Notas"].min())
print("Max: ", df["Notas"].max())
print("Median: ", df["Notas"].median())
print("Var: ", df["Notas"].var())

print("\n\n\n###### DROP & FILL ######")

indices = ["Aluno 1", "Aluno 2", "Aluno 3"]
colunas = ["Nome", "Altura", "Sono Médio"]
dados = [["Anderson Falcon", 173, 7], ["Pedro Tokão", 182, 6], ["Luciano Ô Sampaio", 160, 7]]
df = pd.DataFrame(dados, index=indices, columns=colunas)
print(df)

print("IS Null:", df.isnull(), sep="\n")
print("\nIS Null:", df["Sono Médio"].isnull(), sep="\n")

print("\nNull:", df["Sono Médio"].isnull(), sep="\n")

df.dropna(thresh=2, inplace=True)
print(df)

"---------------------------------------------------------------------------------------------"

#Código com DataFrames novos:
    
df1 = pd.DataFrame(
    {
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    },
    index=[0, 1, 2, 3],
)


df2 = pd.DataFrame(
    {
        "A": ["A4", "A5", "A6", "A7"],
        "B": ["B4", "B5", "B6", "B7"],
        "C": ["C4", "C5", "C6", "C7"],
        "D": ["D4", "D5", "D6", "D7"],
    },
    index=[4, 5, 6, 7],
)


df3 = pd.DataFrame(
    {
        "A": ["A8", "A9", "A10", "A11"],
        "B": ["B8", "B9", "B10", "B11"],
        "C": ["C8", "C9", "C10", "C11"],
        "D": ["D8", "D9", "D10", "D11"],
    },
    index=[8, 9, 10, 11],
)
    
    
print("\n\nConcatenação em Linha: ", pd.concat([df1,df2,df3]), sep="\n") 
print("\n\nConcatenação em Coluna: ", pd.concat([df1,df2,df3], axis=1), sep="\n")    

# merge, key, how = inner 




