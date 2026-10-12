# Séance 3 · La régression et le clustering

Deux problèmes, deux fichiers, deux notebooks.

- **Régression** : Comtoise Auto Occasion voudrait **estimer le prix** d'une voiture dès son arrivée en stock. La réponse à
  deviner est un **nombre**. On calcule d'abord une droite **à la main** sur 5 voitures, puis on la refait sur 500.
- **Clustering** : Comtoise Market, un supermarché, a 600 clients avec une carte de fidélité et **aucune catégorie** de clients.
  On cherche des **groupes** de clients qui se ressemblent, sans réponse connue à l'avance.

Les fichiers sont déjà propres : la préparation a été faite en séances 1 et 2.

## Au programme

**Régression**

- Prédire un **nombre** : régression ou classification ?
- La **droite** à la main : moyennes, écarts, pente, point de départ, prédiction ; d'où viennent les formules
- Mesurer l'erreur : **erreur moyenne**, **RMSE**, **R²**, comparés à un modèle « bête »
- **Plusieurs caractéristiques** à la fois, lire un coefficient « toutes choses égales par ailleurs », les caractéristiques jumelles
- Les **résidus**, la **courbe** (régression polynomiale), trop de courbure : le sur-apprentissage
- Les pièges : extrapolation, valeur aberrante, corrélation et causalité

**Clustering**

- Regrouper sans réponse connue ; la **distance** comme mesure de ressemblance
- **K-Means** à la main sur 9 clients, puis avec scikit-learn ; le tirage des centres de départ
- **Standardiser** d'abord ; **choisir K** (coude, silhouette) ; **lire** les groupes
- En un coup d'œil : le clustering **hiérarchique**, **DBSCAN**, la **PCA**

## Fichiers

| Fichier | Contenu |
|---|---|
| [ELC2 - Séance 3 - La régression.pdf](ELC2%20-%20Séance%203%20-%20La%20régression.pdf) | les slides de régression |
| [ELC2 - Séance 3 - Le clustering.pdf](ELC2%20-%20Séance%203%20-%20Le%20clustering.pdf) | les slides de clustering |
| [seance3-etudiants.zip](seance3-etudiants.zip) | **à télécharger** : les deux notebooks et les fichiers de données |
| [ia-elc2/](ia-elc2/) | les mêmes fichiers, à consulter en ligne : les notebooks s'y affichent **avec leurs résultats** |

Dans `ia-elc2` :

| Fichier | Contenu |
|---|---|
| `04-regression.ipynb` | le notebook de régression, pas à pas |
| `05-clustering.ipynb` | le notebook de clustering, pas à pas |
| `donnees/voitures-comtoise-auto.csv` | 500 voitures d'occasion : année, kilométrage, puissance, carburant, état, prix |
| `donnees/clients-comtoise-market.csv` | 600 clients : âge, visites par mois, panier moyen, part en promotion, part de bio |
| `donnees/formes.csv` | 310 points (deux croissants et des points isolés), pour essayer DBSCAN |

Pour travailler sur votre ordinateur : décompressez l'archive, puis placez les deux notebooks et le dossier `donnees` dans
votre dossier `ia-elc2`. Si un fichier de données manque, le notebook le télécharge tout seul. Dans l'archive, les notebooks
sont vierges : c'est en les exécutant que vous obtenez les résultats.

## Sans rien installer : Google Colab

| Notebook | |
|---|---|
| Régression | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/josephazar/ELC2-Introduction-IA-2026/blob/main/seance-3/ia-elc2/04-regression.ipynb) |
| Clustering | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/josephazar/ELC2-Introduction-IA-2026/blob/main/seance-3/ia-elc2/05-clustering.ipynb) |

Connectez-vous avec un compte Google, puis **Exécution → Tout exécuter**. Pour garder votre
travail : **Copier sur Drive**.

*Entreprises, personnes, voitures et clients fictifs : les données ont été fabriquées pour le cours.*
