# =============================================================================
# TD · Prétraitement des données · le script complet
# ELC2 · Introduction au machine learning
#
# Le même traitement que la partie 9 du notebook 02-td-pretraitement.ipynb, sans
# les explications. Depuis le dossier ia-elc2, dans un terminal :
#
#     Windows        : .venv\Scripts\python td-pretraitement.py
#     macOS, Linux   : .venv/bin/python td-pretraitement.py
# =============================================================================

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler

ORDRE_EDUCATION = {"HighSchool": 0, "Bachelor": 1, "Master": 2, "PhD": 3}

pd.set_option("display.width", 200)          # afficher toutes les colonnes
pd.set_option("display.max_columns", None)


def titre(texte):
    print()
    print(texte)
    print("-" * len(texte))


# --- 1. Regarder avant de toucher --------------------------------------------
data = pd.read_csv("donnees/Data.csv")

titre("1. Le fichier")
print(data.shape[0], "clients,", data.shape[1], "colonnes")
print(data.head(10))
print()
print("Cases vides par colonne :")
print(data.isna().sum())

# --- 2. Séparer les features (X) et la cible (y) ------------------------------
# La cible est en texte : No -> 0, Yes -> 1.
X = data.drop(columns="Purchased")
y = data["Purchased"].map({"No": 0, "Yes": 1})

# --- 3. Encoder les catégories (avant la division) ----------------------------
# Country n'a pas d'ordre : one-hot, une colonne de 0/1 par pays.
# Education a un ordre : on le donne nous-mêmes. (LabelEncoder rangerait les
# diplômes par ordre alphabétique, et Bachelor passerait avant HighSchool.)
X = pd.get_dummies(X, columns=["Country"], dtype=int)
X["Education"] = X["Education"].map(ORDRE_EDUCATION)

titre("3. Encodage")
print("Colonnes :", list(X.columns))

# --- 4. Supprimer la colonne jumelle (avant la division) ----------------------
r = X["Age"].corr(X["Experience"])
X = X.drop(columns="Experience")

titre("4. Corrélation")
print(f"r(Age, Experience) = {r:.3f} : on garde Age, on supprime Experience")

# --- 5. Diviser : 80 % train, 20 % test --------------------------------------
# À partir d'ici, tout ce qui se calcule (médianes, bornes, moyennes) se calcule
# sur le train, puis s'applique tel quel au test : pas de fuite de données.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

titre("5. Division")
print("train :", X_train.shape, "  test :", X_test.shape)

# --- 6. Imputer : fit sur le train, transform sur les deux ---------------------
# La médiane, parce que les salaires ont des valeurs extrêmes.
colonnes_num = ["Age", "Salary"]
imputer = SimpleImputer(strategy="median")
X_train[colonnes_num] = imputer.fit_transform(X_train[colonnes_num])
X_test[colonnes_num] = imputer.transform(X_test[colonnes_num])

titre("6. Imputation")
print("Médianes apprises sur le train :", dict(zip(colonnes_num, imputer.statistics_.tolist())))

# --- 7. Plafonner les salaires extrêmes (règle de Tukey, bornes du train) -------
q1 = X_train["Salary"].quantile(0.25)
q3 = X_train["Salary"].quantile(0.75)
iqr = q3 - q1
basse, haute = q1 - 1.5 * iqr, q3 + 1.5 * iqr

titre("7. Valeurs extrêmes")
print("Bornes apprises sur le train :", basse, "et", haute)
print("Plafonnés dans le train :", sorted(X_train.loc[X_train["Salary"] > haute, "Salary"].tolist()))
print("Plafonnés dans le test  :", sorted(X_test.loc[X_test["Salary"] > haute, "Salary"].tolist()))

X_train["Salary"] = X_train["Salary"].clip(basse, haute)
X_test["Salary"] = X_test["Salary"].clip(basse, haute)

# --- 8. Standardiser : fit sur le train, transform sur les deux ----------------
scaler = StandardScaler()
X_train[colonnes_num] = scaler.fit_transform(X_train[colonnes_num])
X_test[colonnes_num] = scaler.transform(X_test[colonnes_num])

titre("8. Standardisation")
print("Moyennes du train (attendu : 0) :", (X_train[colonnes_num].mean().round(2) + 0.0).tolist())   # + 0.0 : évite « -0.0 »
print("Écarts-types du train (attendu : 1) :", X_train[colonnes_num].std(ddof=0).round(2).tolist())

titre("Les données prêtes (5 premières lignes du train)")
print(X_train.head().round(2))

# --- 9. Le même travail avec un Pipeline scikit-learn ------------------------
X_brut = data.drop(columns=["Purchased", "Experience"])
y = data["Purchased"].map({"No": 0, "Yes": 1})
X_train_b, X_test_b, y_train, y_test = train_test_split(X_brut, y, test_size=0.2, random_state=42)

preparation = ColumnTransformer([
    ("nombres", Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ]), ["Age", "Salary"]),
    ("pays", OneHotEncoder(sparse_output=False, handle_unknown="ignore"), ["Country"]),
    ("diplome", OrdinalEncoder(categories=[list(ORDRE_EDUCATION)]), ["Education"]),
])
X_train_p = preparation.fit_transform(X_train_b)   # fit + transform sur le train
X_test_p = preparation.transform(X_test_b)         # transform seulement sur le test

titre("9. Pipeline scikit-learn")
print("train :", X_train_p.shape, "  test :", X_test_p.shape)
print("Colonnes :", list(preparation.get_feature_names_out()))
