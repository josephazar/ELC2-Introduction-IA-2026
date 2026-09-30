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

## Fichiers

| Fichier | Contenu |
|---|---|
| [ELC2 - Séance 1 - Le machine learning, et ses données.pdf](ELC2%20-%20Séance%201%20-%20Le%20machine%20learning,%20et%20ses%20données.pdf) | les slides |
| [document1-email-nathalie.pdf](document1-email-nathalie.pdf) | le mail de Nathalie, l'extrait du fichier, le tableau à remplir |
| [seance1-etudiants.zip](seance1-etudiants.zip) | **à télécharger** : le dossier `ia-elc2` complet |
| [ia-elc2/](ia-elc2/) | le même contenu, à consulter en ligne |

Dans `ia-elc2` :

| Fichier | Contenu |
|---|---|
| `requirements.txt` | la liste des bibliothèques du cours et de leurs versions |
| `01-premier-notebook.ipynb` | le premier notebook : toutes les étapes du cours, en Python |
| `donnees/ventes-3-agences.xlsx` | le fichier de ventes, avec ses défauts, et son dictionnaire des colonnes |

Pour installer et lancer Jupyter : [installer-jupyter.pdf](../installer-jupyter.pdf).

*Entreprise, personnes et ventes fictives. Les noms de villes sont réels et servent d'étiquettes.*
