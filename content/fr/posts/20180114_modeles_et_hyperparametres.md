---
date: 2018-01-14T11:56:31+01:00
title: "Modèles et hyperparamétres"
categories: [ia]
tags: [scikit-learn]
comments: true
draft: false
---

Hello,  
  
L'un des problèmes lorsque l'on débute en *machine learning* est le choix de l'algorithme (ou modèle) à utiliser. Je viens de tomber sur un [article du blog de Kaggle](http://blog.kaggle.com/2016/07/21/approaching-almost-any-machine-learning-problem-abhishek-thakur/) où l'auteur partage son approche des différents problèmes à résoudre en *ML*. J'ai noté deux parties qui m'ont éclairé un peu plus sur le choix des modèles et des hyperparamètres à régler.


## Choix d'un modèle

Il y a deux grandes familles d'algorithmes : ceux qui permettent de réaliser une prédiction (à l'aide d'une régression) et ceux qui identifie une variable parmi d'autres (la classification). Les modèles les plus courants pour réaliser ses tâches sont donc :


Classification | Regression
:- | -
Random Forest | Random Forest
GBM | GBM
Logistic Regression | Linear Regression
Naive Bayes | Ridge
Support Vector Machines | Lasso
k-Nearest Neighbors | SVR


## Choix des hyperparamètres

Les hyperparamètres sont ces variables qui permettent d'affiner le fonctionnement d'un modèle de *machine learning*. Jusqu'à présent, j'utilisais des valeurs trouvées dans un livre ou sur des sites internet, sans trop savoir qu'est ce que je pouvais utiliser, jusqu'à quelle valeur je pouvais aller.  
Bref, j'y allais à tâtons au "pif-o-mètre". Mais l'auteur partage également un tableau récapitulatif de ces différents hyperparamètres et les plages de valeurs les plus prometteuses.  
Je le reprend ici :


Modèle | Hyperparamètre | Plage de données
 :-------: | :----------------: | :-----------------:
**Régression linéaire** | fit_intercept | True / False
**Régression linéaire** | normalize | True / False
**Ridge** | alpha | 0.01, 0.1, 1.0, 10, 100
**Ridge** | fit_intercept | True / False
**Ridge** | normalize | True / False
**K-neighbors** | N_neighbors | 2, 4, 8, 16...
**K-neighbors** | p | 2,3
**SVM** | C | 0.001, 0.01...10...100...1000
**SVM** | gamma | Auto ou Random Search
**SVM** | class_weight | Balanced, None
**Régression logistique** | Penalty | L1 ou I2
**Régression logistique** | C | 0.001, 0.01...10...100
**Naive Bayes** | aucun | aucun
**Lasso** | alpha | 0.1, 1.0, 10
**Lasso** | normalize | True / False
**Random Forest** | n_estimators | 120, 300, 500, 800, 1200
**Random Forest** | max_depth | 5, 8, 15, 25, 30, None
**Random Forest** | min_samples_split | 1, 2, 5, 10, 15, 100
**Random Forest** | min_samples_leaf | 1, 2, 5, 10
**Random Forest** | max_features | Log2, sqrt, None
**Xgboost** | eta | 0.01, 0.015, 0.025, 0.05, 0.1
**Xgboost** | gamma | 0.05-0.1, 0.3, 0.5, 0.7, 0.9, 1.0
**Xgboost** | max_depth | 3, 5, 7, 9, 12, 15, 17, 25
**Xgboost** | min_child_weight | 1, 3, 5, 7
**Xgboost** | subsample | 0.6, 0.7, 0.8, 0.9, 1.0
**Xgboost** | colsample_bytree | 0.6, 0.7, 0.8, 0.9, 1.0
**Xgboost** | lambda | 0.01-0.1, 1.0, Random Search
**Xgboost** | alpha | 0, 0.1, 0.5, 1.0, Random Search


J'espère que ces petits récapitulatifs vous seront autant utiles qu'à moi ;-)

A bientôt !

