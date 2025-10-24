import pandas as pd

#Leitura do dataset
df = pd.read_csv('../data/googleplaystore.csv')

#Remoção de duplicatas
df_clean = df.drop_duplicates()

# Preenchendo valores nulos de 'Rating' com a média
df_clean['Rating'] = df_clean['Rating'].fillna(df_clean['Rating'].mean())

# Preenchendo valores nulos de 'Type' com o 'Unknown' e substituindo '0' por 'Free'
df_clean['Type'] = df_clean['Type'].fillna('Unknown').replace('0', 'Free')

# Preenchendo valores nulos de 'Content Rating' com o 'Unrated'
df_clean['Content Rating'] = df_clean['Content Rating'].fillna('Unrated')

# Preenchendo valores nulos de 'Current Ver' com o 'Varies with device'
df_clean['Current Ver'] = df_clean['Current Ver'].fillna('Varies with device')

# Preenchendo valores nulos de 'Android Ver' com o 'Varies with device'
df_clean['Android Ver'] = df_clean['Android Ver'].fillna('Varies with device')

# Explodindo 'Genres' para múltiplas linhas
df_clean['Genres'] = df_clean['Genres'].astype(str)
df_clean['Genres'] = df_clean['Genres'].str.split(';')
df_exploded = df_clean.explode('Genres').reset_index(drop=True)

# Removendo tupla com valores inconsistentes
df_exploded = df_exploded[df_exploded['Genres'] != 'February 11, 2018']  # mantém só os outros valores

# Removendo caracteres especiais e convertendo tipos de dados
df_exploded['Installs'] = df_exploded['Installs'].astype(str)
df_exploded['Installs'] = df_exploded['Installs'].str.replace('[+,]', '', regex=True)
df_exploded['Installs'] = df_exploded['Installs'].astype(int)

df_exploded['Rating'] = df_exploded['Rating'].round(2)

# Removendo caracteres especiais e convertendo tipos de dados
df_exploded['Price'] = df_exploded['Price'].astype(str)
df_exploded['Price'] = df_exploded['Price'].str.replace('[$]', '', regex=True)
df_exploded['Price'] = df_exploded['Price'].astype(float)
df_exploded['Price'] = df_exploded['Price'].round(2)

# Padronizando formatação da coluna 'Category'
df_exploded['Category'] = df_exploded['Category'].str.replace('_', ' ').str.title()

print(df_exploded.head())