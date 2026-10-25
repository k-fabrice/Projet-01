# Librairies
import pandas as pd
from ydata_profiling import ProfileReport

# Lecture de données

import pandas as pd
from ydata_profiling import ProfileReport

# 1. Charger les données
df = pd.read_csv(r"D:\EME_2\donnees_m01\produits.csv")

# 2. Générer le rapport d'analyse exploratoire
profile = ProfileReport(
    df,
    title="Analyse exploratoire des données",
    explorative=True
)

# 3. Enregistrer le rapport au format HTML
profile.to_file(r"D:\EME_2\rapport_profilage.html")

print("Rapport créé avec succès !")
print("Emplacement : D:\\EME_2\\rapport_profilage.html")


