# Librairies
import pandas as pd

# Lecture de données
data=pd.read_csv (r"D:\EME_2\donnees_m01\produits.csv")

print(data.head(10))

df=data.copy()

missing = df.isnull().sum()
print(missing)


