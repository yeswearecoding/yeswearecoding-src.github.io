---
date: 2018-01-14T11:56:31+01:00
title: "Modèles et hyperparamétres"
comments: true
draft: false
---
{{% jupyter_cell_start markdown %}}

Hello,  
  
L'un des problèmes lorsque l'on débute en *machine learning* est le choix de l'algorithme (ou modèle) à utiliser. Je viens de tomber sur un [article du blog de Kaggle](http://blog.kaggle.com/2016/07/21/approaching-almost-any-machine-learning-problem-abhishek-thakur/) où l'auteur partage son approche des différents problèmes à résoudre en *ML*. J'ai noté deux parties qui m'ont éclairé un peu plus sur le choix des modèles et des hyperparamètres à régler.

{{% jupyter_cell_end %}}{{% jupyter_cell_start markdown %}}

## Choix d'un modèle

Il y a deux grandes familles d'algorithmes : ceux qui permettent de réaliser une prédiction (à l'aide d'une régression) et ceux qui identifie une variable parmi d'autres (la classification). Les modèles les plus courants pour réaliser ses tâches sont donc :

{{% jupyter_cell_end %}}{{% jupyter_cell_start markdown %}}

Classification | Regression
:- | -
Random Forest | Random Forest
GBM | GBM
Logistic Regression | Linear Regression
Naive Bayes | Ridge
Support Vector Machines | Lasso
k-Nearest Neighbors | SVR

{{% jupyter_cell_end %}}{{% jupyter_cell_start markdown %}}

## Choix des hyperparamètres

Les hyperparamètres sont ces variables qui permettent d'affiner le fonctionnement d'un modèle de *machine learning*. Jusqu'à présent, j'utilisais des valeurs trouvées dans un livre ou sur des sites internet, sans trop savoir qu'est ce que je pouvais utiliser, jusqu'à quelle valeur je pouvais aller.  
Bref, j'y allais à tâtons au "pif-o-mètre". Mais l'auteur partage également un tableau récapitulatif de ces différents hyperparamètres et les plages de valeurs les plus prometteuses.  
Je le reprend ici :

{{% jupyter_cell_end %}}{{% jupyter_cell_start markdown %}}

Modèle | Hyperparamètre | Plage de données
 :-------: | :----------------: | :-----------------:
**Régression linéaire** | fit_intercept<br>normalize | True / False<br>True / False
**Ridge** | alpha<br>fit_intercept<br>normalize | 0.01, 0.1, 1.0, 10, 100<br>True / False<br>True / False
**K-neighbors** | N_neighbors<br>p | 2, 4, 8, 16...<br>2,3
**SVM** | C<br>gamma<br>class_weight | 0.001, 0.01...10...100...1000<br>Auto ou Random Search<br>Balanced, None
**Régression logistique** | Penalty<br>C | L1 ou I2<br>0.001, 0.01...10...100
**Naive Bayes** | aucun | aucun
**Lasso** | alpha<br>normalize | 0.1, 1.0, 10<br>True / False
**Random Forest** | n_estimators<br>max_depth<br>min_samples_split<br>min_samples_leaf<br>max_features | 120, 300, 500, 800, 1200<br>5, 8, 15, 25, 30, None<br>1, 2, 5, 10, 15, 100<br>1, 2, 5, 10<br>Log2, sqrt, None
**Xgboost** | eta<br>gamma<br>max_depth<br>min_child_weight<br>subsample<br>colsample_bytree<br>lambda<br>alpha | 0.01, 0.015, 0.025, 0.05, 0.1<br>0.05-0.1, 0.3, 0.5, 0.7, 0.9, 1.0<br>3, 5, 7, 9, 12, 15, 17, 25<br>1, 3, 5, 7<br>0.6, 0.7, 0.8, 0.9, 1.0<br>0.6, 0.7, 0.8, 0.9, 1.0<br>0.01-0.1, 1.0, Random Search<br>0, 0.1, 0.5, 1.0, Random Search


{{% jupyter_cell_end %}}{{% jupyter_cell_start markdown %}}

J'espère que ces petits récapitulatifs vous seront autant utiles qu'à moi ;-)

A bientôt !

{{% jupyter_cell_end %}}