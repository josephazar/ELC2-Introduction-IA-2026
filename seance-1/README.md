# Séance 1 · Le machine learning, et ses données

Comtoise Auto Occasion veut estimer ses prix de reprise par machine learning. Son prestataire
refuse le fichier de ventes : doublons, écritures différentes pour une même agence, nombres
saisis comme du texte, valeurs impossibles, cases vides. Nous le préparons étape par étape.

## Au programme

- Ce qu'est le machine learning : apprendre une règle à partir d'exemples
- Exemple, caractéristique, cible ; classer, prédire un nombre, regrouper
- Lire une colonne : les **distributions**, moyenne et médiane, écart-type, quartiles, formes courantes, règle 68-95-99,7
- Lire deux colonnes : la **corrélation**, et pourquoi ne garder qu'une colonne sur deux jumelles
- Les **valeurs aberrantes** : bornes métier, z-score, quartiles (règle de Tukey), et quand utiliser quoi
- Les **cases vides** : supprimer, remplir, « Inconnu »
- **Encoder** le texte : ordinal ou one-hot
- **Mettre à l'échelle** : normaliser ou standardiser

## TD · Prétraitement des données

Un fichier de 50 clients (`Data.csv`) et cinq problèmes : valeurs manquantes, valeurs
aberrantes, variables catégorielles, colonnes corrélées, échelles différentes. Chaque calcul
se fait d'abord au crayon, puis en Python. Le notebook `02-td-pretraitement.ipynb` refait tout
le TD pas à pas, avec ses explications, et se termine par le prétraitement complet : division
train / test, `fit` sur le train, `transform` sur le test.

## Fichiers

| Fichier | Contenu |
|---|---|
| [ELC2 - Séance 1 - Le machine learning, et ses données.pdf](ELC2%20-%20Séance%201%20-%20Le%20machine%20learning,%20et%20ses%20données.pdf) | les slides |
| [document1-email-nathalie.pdf](document1-email-nathalie.pdf) | le mail de Nathalie, l'extrait du fichier, le tableau à remplir |
| [TD - Prétraitement des données - Atelier pratique.pdf](TD%20-%20Prétraitement%20des%20données%20-%20Atelier%20pratique.pdf) | le TD |
| [seance1-etudiants.zip](seance1-etudiants.zip) | **à télécharger** : le dossier `ia-elc2` complet |
| [ia-elc2/](ia-elc2/) | le même contenu, à consulter en ligne : les notebooks y sont affichés **avec leurs résultats** |

Dans `ia-elc2` :

| Fichier | Contenu |
|---|---|
| `requirements.txt` | la liste des bibliothèques du cours et de leurs versions |
| `01-premier-notebook.ipynb` | le premier notebook : toutes les étapes du cours, en Python |
| `02-td-pretraitement.ipynb` | le TD, pas à pas : du calcul au crayon au code |
| `td-pretraitement.py` | le prétraitement complet du TD, en un script : `uv run python td-pretraitement.py` |
| `donnees/ventes-3-agences.xlsx` | le fichier de ventes, avec ses défauts, et son dictionnaire des colonnes |
| `donnees/Data.csv` | le fichier de clients du TD |

Dans l'archive, les notebooks sont vierges : c'est en les exécutant que vous obtenez les
résultats.

Pour installer et lancer Jupyter : [installer-jupyter.pdf](../installer-jupyter.pdf).

*Entreprise, personnes et ventes fictives. Les noms de villes sont réels et servent d'étiquettes.*
