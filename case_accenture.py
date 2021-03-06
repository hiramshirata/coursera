import pandas as pd

csv_path = 'C:\\Users\\Yugur\\Downloads\\poli-piegraph-mar15.csv'

df = pd.read_csv(csv_path)

print(df.groupby(by=['Origem']).sum().sort_values(by=['Receita'], ascending=False))