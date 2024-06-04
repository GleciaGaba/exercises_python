import pandas as pd

# Ler o arquivo Excel para um DataFrame
df_homonimias = pd.read_excel("/Users/Bazinga/Documents/python_2024/formation_python/Nomes_e_Sobrenomes_Com_IDs_Ajustado.xlsx")

# Criar uma coluna "Nome Completo" concatenando nome e sobrenome
df_homonimias['Nome Completo'] = df_homonimias['Nome'] + " " + df_homonimias['Sobrenome']

# Contar a frequência dos nomes completos
frequencias = df_homonimias['Nome Completo'].value_counts()

# Identificar homonímias (nomes completos com mais de uma ocorrência)
homonimias = frequencias[frequencias > 1]

# Criar um dicionário para armazenar os resultados das homonímias e seus respectivos IDs
homonimias_detalhes = {}

# Iterar sobre cada nome completo identificado como homonímia
for nome_completo in homonimias.index:
    # Encontrar os índices (IDs) onde cada homonímia ocorre
    ids = df_homonimias[df_homonimias['Nome Completo'] == nome_completo].index.tolist()
    # Adicionar os detalhes ao dicionário
    homonimias_detalhes[nome_completo] = ids

# Exibir os detalhes das homonímias encontradas
print(homonimias_detalhes)
