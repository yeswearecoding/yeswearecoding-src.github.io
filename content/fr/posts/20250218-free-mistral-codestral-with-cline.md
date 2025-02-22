---
title: "Utiliser gratuitement Mistral Codestral"
date: 2025-02-18T18:54:43+01:00
draft: false
tags: ["ia", "LLM"]
categories: ["ia"]
slug: "free-mistral-codestral"
---

Hello ! 👋

J'ai trouvé comment utiliser Codestral, le modèle de Mistral AI dédié au code, gratuitement. Je vous montre comment le paramétrer dans Cline, un outil de génération de code grâce à l'IA.

## Codestral, c'est quoi au juste ? 🤔

Codestral est le premier modèle de Mistral AI spécialement conçu pour la génération de code. Il supporte plus de 80 langages de programmation, des plus courants comme Python, Java ou JavaScript jusqu'aux plus spécifiques comme Swift ou Fortran.

Concrètement, il permet de :
- Compléter des fonctions de code
- Générer des tests
- Compléter du code partiel avec un mécanisme de "fill-in-the-middle"

## L'outil qui va nous aider : Cline 🛠️

Pour utiliser Codestral facilement, nous allons passer par Cline, une extension VSCode qui va nous simplifier la vie. C'est un assistant de code, assez complet, qui permet (selon la [doc du projet Github](https://github.com/cline/cline)) :

- Analyser intelligemment vos projets en comprenant la structure des fichiers
- Créer et modifier des fichiers (avec votre permission bien sûr)
- Exécuter des commandes dans le terminal
- Même déboguer des problèmes visuels pour le développement web !

Cline vous demande toujours la permission avant de faire des modifications, sauf si vous le laissez faire (bon, je ne conseille pas vraiment). Pour ma part, je l'ai autorisé à lire tous les fichiers locaux, et je valide les modifications de code et les commandes shell (*Auto-approve: Read files and directories*) .

D'ailleurs, si jamais vous avez des soucis d'intégration de shell comme moi (oui Cline n'aime pas les *shell* un peu trop verbeaux avec pleins de smileys genre Zsh + Oh-my-zsh ^^), je vous mets le lien vers la doc pour fixer ça : [shell-integration-problems](https://github.com/saoudrizwan/shell-integration-problems). J'utilise depuis un *Bash* classique, sans fioritures.

## La mise en place, étape par étape ⚙️

Même si Cline propose d'utiliser directement une clé API de Mistral, cela ne fonctionne pas avec la clé Codestral (pour le moment, espérons que ça soit fixé un jour). La méthode repose donc sur [liteLLM](https://github.com/BerriAI/litellm) qui sert de proxy.

Je vous montre ici comment faire pour Codestral mais cette méthode qui passe par un proxy permet d'utiliser n'importe quel *provider* supporté par **LiteLLM**, ce qui peut être utile dans plein d'autres cas :).

### 1. Obtenir une clé API Mistral

Première étape indispensable : avoir une clé Mistral

1. Créez un compte sur la plateforme [Mistral](https://console.mistral.ai/codestral) ;
2. Acceptez les conditions d'utilisation ;
3. Récupérez votre clé API dans les paramètres (Menu Codestral -> Codestral).

A noter que le code que vous envoyez pourra être utilisé par les équipes de Mistral (donc n'envoyez pas tout et n'importe quoi, surtout pas de *secrets* !!)

### 2. Installer litellm

On commence par installer [liteLLM](https://github.com/BerriAI/litellm) qui va nous servir de pont avec Codestral :

```bash
pip install 'litellm[proxy]'
```

### 3. Configurer et lancer litellm

Une fois l'installation terminée :

```bash
# Exportez votre clé API
export CODESTRAL_API_KEY=[votre_clé_API]

# Lancez le serveur
litellm --model codestral/codestral-latest
```

### 4. Installer et configurer Cline dans VSCode

#### Installation

C'est une extension, il suffit donc d'aller la chercher dans la *marketplace*.

#### Configuration

Ouvrez l'extension Cline qui s'est ajoutée dans votre barre latérale et :

1. Affichez les paramètres (la roue dentée - classique -) ;
2. Pour les valeurs :
   - Provider : "OpenAPI Compatible"
   - Base URL : `http://0.0.0.0:4000`
   - API Key : mettez au moins un caractère (c'est obligatoire mais pas utilisé)
   - Model ID : `codestral-latest`

Comme je ne suis pas vraiment *fluent*, dans *Custom Instructions* je mets `Speak in french` pour converser en français.

Validez en cliquant sur le bouton **Done**.

## Et voilà ! 🎉

Vous avez maintenant un environnement de développement boosté à l'IA, gratuitement.

Je découvre encore Cline et je l'utilise en mode *Act* (à choisir tout en bas à droite), avec autorisation de lire les fichiers  et je valide manuellement ses propositions.

J'utilise ces outils depuis quelques jours et je dois dire que je suis assez bluffé : c'est un vrai gain de productivité. Le fait que ce soit gratuit et que ça s'intègre parfaitement à VSCode en fait une solution vraiment intéressante pour les développeurs, l'IA fait de sacré progrès dans ce domaine 😱 !

Bonnes sessions de codage ! 🚀
