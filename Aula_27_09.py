import pandas as pd

indices = ["The Pacific", "Black Mirror", "CSI", "NCIS", "Lost"]
colunas = ["Nota", "Temporadas", "Episódios"]
dados = [[8.3, 1, 10], [8.7, 6, 27], [7.7, 15, 337], [6.9, 14, 458], [8.3, 6, 121]]
df = pd.DataFrame(dados, index = indices, columns = colunas)
df.drop("Lost", axis=0, inplace=True)
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






-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------







import pandas as pd

df = pd.read_csv("microdados_ed_basica_2021", encoding="unicode_escape", engine="python", sep=";")

print(df.head())
print(df.tail())

df.drop(columns=df.loc[:, "CO_MICRORREGIAO":"DT_ANO_LETIVO_TERMINO"], inplace=True)

print(df.head())
print(df.tail())

df.to_csv("mais_facil.csv", index=False)









