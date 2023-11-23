import pandas as pd

# Chargement des données depuis l'URL
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
df = pd.read_csv(url)

# Calcul du ratio sepal_width/sepal_length
df['sepal_ratio'] = df['sepal_width'] / df['sepal_length']

# Filtrer le dataframe pour garder uniquement les ratios < 0.7
df_filtered = df[df['sepal_ratio'] < 0.7]


# Exporter le DataFrame filtré vers un fichier CSV
df_filtered.to_csv('data_filtered.csv', index=False)