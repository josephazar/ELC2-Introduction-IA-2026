# Séance 2 · La classification

Comtoise Télécom veut repérer ses clients qui vont résilier. Pour chaque client, il faut prédire
une catégorie : *résilie* ou *reste*. On refait la préparation des données de la séance 1, on
découpe le fichier en train et test, puis on classe et on mesure.

## Au programme

- Ce qu'est la classification : prédire une **catégorie**, binaire ou multi-classe
- **KNN**, **régression logistique**, **arbres de décision** : à la main, puis avec scikit-learn
- Mesurer un classifieur : **matrice de confusion**, accuracy, precision, recall, F1
- Les pièges : classes déséquilibrées, sur-ajustement, mise à l'échelle oubliée
- Le rappel de la préparation : doublons, variable dépendante et variables indépendantes,
  distributions, valeurs aberrantes (z-score ou quartiles), cases vides, standardisation,
  encodage ordinal et one-hot
- **Train et test** : `fit` sur le train, `transform` sur le test, `Pipeline`

## Fichiers

| Fichier | Contenu |
|---|---|
| [ELC2 - Séance 2 - La classification.pdf](ELC2%20-%20Séance%202%20-%20La%20classification.pdf) | les slides |
| [seance2-etudiants.zip](seance2-etudiants.zip) | **à télécharger** : le notebook et son fichier de données |
| [ia-elc2/](ia-elc2/) | les mêmes fichiers, à consulter en ligne : le notebook s'y affiche **avec ses résultats** |

Dans `ia-elc2` :

| Fichier | Contenu |
|---|---|
| `03-classification.ipynb` | le notebook : la préparation des données, puis la classification |
| `donnees/clients-comtoise-telecom.xlsx` | les clients, avec leurs défauts, et un dictionnaire des colonnes |

Pour travailler sur votre ordinateur : décompressez l'archive, puis placez `03-classification.ipynb`
et le dossier `donnees` dans votre dossier `ia-elc2`, celui de la séance 1. Si le fichier de données
manque, le notebook le télécharge tout seul. Dans l'archive, le notebook est vierge : c'est en
l'exécutant que vous obtenez les résultats.

## Sans rien installer : Google Colab

| Notebook | |
|---|---|
| Classification | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/josephazar/ELC2-Introduction-IA-2026/blob/main/seance-2/ia-elc2/03-classification.ipynb) |

Connectez-vous avec un compte Google, puis **Exécution → Tout exécuter**. Pour garder votre
travail : **Copier sur Drive**.

*Entreprise, personnes et clients fictifs. Les noms de villes sont réels et servent d'étiquettes.*
