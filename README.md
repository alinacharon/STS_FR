# Projet d'Analyse de Sons FR 🇫🇷 


Ce projet permet d'analyser des sons à partir d'un fichier CSV nommé `SOUNDBOARD.csv`. Il génère des visualisations basées sur les évaluations et les mots clés associés à chaque son.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé Python sur votre machine. Vous pouvez télécharger Python à partir du site officiel :

- [Télécharger Python](https://www.python.org/downloads/)

### Installation de Python

1. Allez sur le site [python.org](https://www.python.org/downloads/).
2. Cliquez sur le bouton "Download" pour la dernière version de Python.
3. Suivez les instructions d'installation pour votre système d'exploitation (Windows, macOS, Linux).
4. Assurez-vous de cocher l'option "Add Python to PATH" lors de l'installation.

### Installation de pip

Pip est généralement inclus avec les versions récentes de Python. Si vous devez l'installer manuellement :

 Exécutez la commande suivante :
   ```bash
   curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
   python3 get-pip.py
   ```

## Clonage du dépôt

1. Ouvrez un terminal ou une invite de commande.
2. Utilisez la commande suivante pour cloner le dépôt et installer les dépendances:
   ```bash
   git clone https://github.com/alinacharon/STS_ENG.git
   cd STS_ENG
   pip install -r requirements.txt
   ```

## Exécution du projet

1. Assurez-vous que le fichier `SOUNDBOARD.csv` est présent dans le même répertoire que `app.py`.
2. Exécutez le script Python :
   ```bash
   python3 app.py
   ```
3. Le programme analysera les données et générera des visualisations dans un dossier nommé `visualizations`.

## Résultats

Les résultats de l'analyse seront sauvegardés dans un fichier CSV nommé `analysis_results.csv`. Les visualisations pour chaque son seront enregistrées sous forme d'images PNG dans le dossier `visualizations`.
# STS_ENG
