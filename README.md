# Projet d'Analyse de Sons

Ce projet permet d'analyser des sons à partir d'un fichier CSV nommé `SOUNDBOARD.csv`. Il génère des visualisations basées sur les évaluations et les mots clés associés à chaque son.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé Python sur votre machine. Vous pouvez télécharger Python à partir du site officiel :

- [Télécharger Python](https://www.python.org/downloads/)

### Installation de Python

1. Allez sur le site [python.org](https://www.python.org/downloads/).
2. Cliquez sur le bouton "Download" pour la dernière version de Python.
3. Suivez les instructions d'installation pour votre système d'exploitation (Windows, macOS, Linux).
4. Assurez-vous de cocher l'option "Add Python to PATH" lors de l'installation.


## Clonage du dépôt

1. Ouvrez un terminal ou une invite de commande.
2. Utilisez la commande suivante pour cloner le dépôt (remplacez `VOTRE_URL` par l'URL de votre dépôt) :
   ```bash
   git clone VOTRE_URL
   ```
3. Naviguez dans le dossier du projet :
   ```bash
   cd STS_FR
   ```
## Installation des dépendances

1. Ouvrez un terminal ou une invite de commande.
2. Naviguez jusqu'au répertoire où se trouve le fichier `app.py`.
3. Créez un environnement virtuel (optionnel mais recommandé) :
   ```bash
   python3 -m venv venv
   ```
4. Activez l'environnement virtuel :
   - Sur Windows :
     ```bash
     venv\Scripts\activate
     ```
   - Sur macOS/Linux :
     ```bash
     source venv/bin/activate
     ```
5. Installez les dépendances nécessaires en utilisant le fichier `requirements.txt` :
   ```bash
   pip install -r requirements.txt
   ```

## Exécution du projet

1. Assurez-vous que le fichier `SOUNDBOARD.csv` est présent dans le même répertoire que `app.py`.
2. Exécutez le script Python :
   ```bash
   python app.py
   ```
3. Le programme analysera les données et générera des visualisations dans un dossier nommé `visualizations`.

## Résultats

Les résultats de l'analyse seront sauvegardés dans un fichier CSV nommé `analysis_results.csv`. Les visualisations pour chaque son seront enregistrées sous forme d'images PNG dans le dossier `visualizations`.


# STS_FR
