import numpy as np
import pandas as pd

print("#### Criando DATAFRAMES ####")
indices = ["The Pacific", "Black Mirror", "CSI", "NCIS", "Lost"]
colunas = ["Notas", "Temporadas", "Episódios"]
dados = [[8.3, 1, 10], [8.7, 6, 27], [7.7, 15, 337], [6.9, 14, 458], [8.3, 6, 121]]
df = pd.DataFrame(dados, index=indices, columns=colunas)
print(df, end="\n\n")

###########################################################################################
print("##### Seleção #####")
#Selecionando coluna
print("Notas:")
print(df["Notas"], end="\n\n")
#print(df.Nota, end="\n\n") #SQL não vale a pena

#Selecionando colunas
print("Temporadas e Episódios:")
print(df[["Temporadas", "Episódios"]], end="\n\n")

###########################################################################################
print("##### Loc ILOC #####")
#Selecionando linha
print("The Pacific:")
print(df.loc["The Pacific"], end="\n\n")
print(df.iloc[0], end="\n\n")

print("The Pacific, temporadas:", end="")
print(df.loc["The Pacific", "Temporadas"], end="\n\n")

###########################################################################################
print("##### SELEÇÃO COMBINADA #####")
#Pegando elementos de uma coluna
print(df.loc[["The Pacific", "Black Mirror"], "Temporadas"], end="\n\n")

#Pegando elementos de duas colunas
print(df.loc[["The Pacific", "Black Mirror"], ["Temporadas", "Notas"]], end="\n\n")

#Pegando duas colunas inteiras
print(df.loc[:, ["Temporadas", "Notas"]], end="\n\n")
print(type(df.loc[:, ["Temporadas", "Notas"]]))
print(type(df.loc["NCIS"]), end="\n\n")

###########################################################################################
print("##### TIPOS DE OBJETOS #####")
print(df.columns)
print(type(df.columns), end="\n\n")
print(df.columns.values)
print(type(df.columns.values), end="\n\n")

print(df.index)
print(type(df.index), end="\n\n")
print(df.index.values)
print(type(df.index.values), end="\n\n")

###########################################################################################
print("##### RETIRANDO LINHAS E COLUNAS #####")
#Adicionando uma coluna extra
df["Coluna Extra"] = df["Notas"] * 2
print(df, end="\n\n")

#Retirando essa mesma coluna de um DataFrame parecido
df2 = df.drop("Coluna Extra", axis=1)
print(df2, end="\n\n")

#Retirando uma coluna do DataFrame original
df.drop("Coluna Extra", axis=1, inplace=True)
print(df, end="\n\n")

#Retirando uma linha
df.drop("Lost", axis=0, inplace=True)
print(df, end="\n\n")

print(df.shape)

###########################################################################################
print("##### SELEÇÃO CONDICIONAL #####")
#Fazendo em todo o df
print(df>3)

#Fazendo em uma coluna
print(df["Notas"]>8, end="\n\n")
print(df[df["Notas"]>8], end="\n\n")

###########################################################################################
print("##### SELEÇÃO CONDICIONAL + SELEÇÃO MÚLTIPLA #####")
print(df[df["Notas"]>8]["Temporadas"], end="\n\n")
print(df[df["Notas"]>8][["Temporadas", "Episódios"]], end="\n\n")

print(df[(df["Notas"]>8) & (df["Temporadas"]>3)])








