import pandas as pd


df = pd.read_csv('Rol_Procedimentos.csv')

df.rename(columns={'OD': 'Odontologia', 'AMB': 'Ambulatorial'}, inplace=True)

df.to_csv('Rol_Procedimentos.csv', index=False)

# Exibir no console
df = pd.read_csv('Rol_Procedimentos.csv')
print(df.head())
print(df.to_string())