import pandas as pd
import numpy as np
from collections import Counter
import re
import matplotlib.pyplot as plt
import seaborn as sns
import os
from ast import literal_eval
import json
from wordcloud import WordCloud

# Set the style
sns.set_theme(style="whitegrid")
sns.set_palette("deep")
plt.rcParams['font.sans-serif'] = ['Helvetica', 'Arial']
plt.rcParams['font.family'] = 'sans-serif'

import pandas as pd

# Étape 1 : Charger les données
def load_data():
    try:
        return pd.read_csv('SOUNDBOARD.csv')
    except FileNotFoundError:
        print("\033[91mPour lancer l'analyse, veuillez placer le fichier dans le dossier avec le code et vérifier qu'il s'appelle bien SOUNDBOARD.\033[0m")

# Étape 2 : Définir les colonnes pour l'analyse
def define_columns(df):
    attractiveness_columns = [
        col for col in df.columns if col.startswith("Sur une échelle de 1 à 7")
    ]
    keyword_columns = [
        col for col in df.columns if col.startswith("Le(s) mot(s) clés que vous attribueriez")
    ]
    
    return attractiveness_columns, keyword_columns

# Fonction pour obtenir tous les mots clés avec leur fréquence
def get_all_keywords(df, column):
    all_keywords = [kw.strip() for keywords in df[column].dropna()
                    for kw in keywords.split(',')]
    return Counter(all_keywords)

# Fonction pour obtenir la liste complète des évaluations
def get_full_rating_list(df, column):
    return df[column].dropna().tolist()

# Fonction pour extraire le numéro du son à partir du nom de la colonne
def extract_sound_number(column_name):
    match = re.search(r'\((\d+)\)', column_name)
    return match.group(1) if match else None

# Fonction pour calculer la note moyenne
def calculate_average_rating(df, column):
    total_sum = df[column].sum()
    total_count = df[column].count()
    return total_sum / total_count if total_count != 0 else 0

# Étape 3 : Analyse pour chaque son
def analyze_sounds(df, attractiveness_columns, keyword_columns):
    results = {}
    min_length = min(len(attractiveness_columns), len(keyword_columns))  # Определяем минимальную длину
    for i in range(min_length):
        sound_number = extract_sound_number(attractiveness_columns[i])
        if sound_number:
            sound_name = f"Son {sound_number}"
            attractiveness_col = attractiveness_columns[i]
            keyword_col = keyword_columns[i]

            results[sound_name] = {
                "Note Moyenne d'Attractivité": calculate_average_rating(df, attractiveness_col),
                "Distribution des Évaluations": get_full_rating_list(df, attractiveness_col),
                "Tous les Mots Clés": get_all_keywords(df, keyword_col)
            }
    
    if not results:
        print("Aucun résultat trouvé. Vérifiez les colonnes d'attractivité et de mots clés.")
    
    return results


# Étape 4 : Sauvegarder les résultats dans un fichier CSV
def save_results(results):
    if not results:
        print("Les résultats sont vides. Aucune sauvegarde effectuée.")
        return
    
    results_df = pd.DataFrame(results).T
    results_df.columns = ['Average Attractiveness Rating', 'Distribution of Ratings', 'All Keywords']
    results_df.to_csv('analysis_results.csv')
    print("\nLes résultats de l'analyse ont été sauvegardés dans 'analysis_results.csv'")

# Visualisation des résultats
def create_visualizations(results_df):
    # Créer le dossier 'visualizations' s'il n'existe pas
    os.makedirs('visualizations', exist_ok=True)

    # Создание визуализаций для каждого звука
    for sound in results_df.index:
        create_visualizations_for_sound(sound, results_df)

print("\033[92mToutes les visualisations ont été générées dans le dossier 'visualizations'.\033[0m")
def safe_eval(x):
    if isinstance(x, list):
        return x
    if isinstance(x, str):
        try:
            return literal_eval(x)
        except:
            try:
                return json.loads(x)
            except:
                try:
                    return dict(Counter(eval(x)))
                except:
                    print(f"Unable to convert: {x}")
                    return {}
    return x

def create_visualizations_for_sound(sound, results_df):
    fig, axs = plt.subplots(2, 2, figsize=(20, 20))
    fig.suptitle(f"Analyse de {sound}", fontsize=24, fontweight='bold', y=0.95)
    
    # 1. Average rating and response distribution
    average = results_df.loc[sound, 'Average Attractiveness Rating']
    distribution = results_df.loc[sound, 'Distribution of Ratings']

    # Create a full list of ratings from 1 to 7
    rating_counts = Counter(distribution)
    full_distribution = [rating_counts.get(i, 0) for i in range(1, 8)]

    # Create a color palette for 7 ratings
    colors = sns.color_palette("husl", 7)

    # Create a bar plot with different colors for each rating
    bars = axs[0, 0].bar(range(1, 8), full_distribution, color=colors)

    axs[0, 0].set_title(f"Distribution des Évaluations\nMoyenne: {average:.2f}/7", fontsize=18)
    axs[0, 0].set_xlabel("Évaluation", fontsize=14)
    axs[0, 0].set_ylabel("Nombre de Réponses", fontsize=14)
    axs[0, 0].set_xlim(0.5, 7.5)
    axs[0, 0].set_xticks(range(1, 8))
    axs[0, 0].set_xticklabels(range(1, 8))

    # Add "0" label for ratings with zero value
    for bar in bars:
        height = bar.get_height()
        if height == 0:
            axs[0, 0].text(bar.get_x() + bar.get_width()/2., height,
                           '', ha='center', va='bottom')

    # 2. Total number of respondents
    total_respondents = len(distribution)
    axs[0, 0].text(0.5, -0.15, f"Nombre Total de Répondants: {total_respondents}", 
                   horizontalalignment='center', transform=axs[0, 0].transAxes, fontsize=14)
    
    # 3. Number of people attributing each keyword
    all_keywords = results_df.loc[sound, 'All Keywords']
    if isinstance(all_keywords, dict):
        keywords = list(all_keywords.keys())
        occurrences = list(all_keywords.values())
    elif isinstance(all_keywords, list):
        if all(isinstance(item, tuple) for item in all_keywords):
            keywords, occurrences = zip(*all_keywords)
        else:
            keywords = all_keywords
            occurrences = [1] * len(keywords)
    else:
        print(f"Unexpected format for 'All Keywords' for {sound}: {type(all_keywords)}")
        keywords = []
        occurrences = []

    if keywords:
        sns.barplot(x=keywords, y=occurrences, ax=axs[0, 1], palette="YlGnBu")
        axs[0, 1].set_title("Occurrences des Mots Clés", fontsize=18)
        axs[0, 1].set_xlabel("Mots Clés", fontsize=14)
        axs[0, 1].set_ylabel("Nombre d'Attributions", fontsize=14)
        axs[0, 1].tick_params(axis='x', rotation=45)
    else:
        axs[0, 1].text(0.5, 0.5, "Aucun mot clé disponible", ha='center', va='center', fontsize=14)
        axs[0, 1].axis('off')

    # 4. Word cloud for all keywords
    if isinstance(all_keywords, dict):
        wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='viridis').generate_from_frequencies(all_keywords)
        axs[1, 0].imshow(wordcloud, interpolation='bilinear')
        axs[1, 0].set_title("Nuage de Mots Clés", fontsize=18)
    elif keywords:
        wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='viridis').generate(' '.join(keywords))
        axs[1, 0].imshow(wordcloud, interpolation='bilinear')
        axs[1, 0].set_title("Nuage de Mots Clés", fontsize=18)
    else:
        axs[1, 0].text(0.5, 0.5, "Aucun mot clé disponible", ha='center', va='center', fontsize=14)
    axs[1, 0].axis('off')
    
    # 5. Rating distribution (violin plot)
    ratings = distribution
    
    sns.violinplot(y=ratings, ax=axs[1, 1], inner="box", color="skyblue")
    axs[1, 1].set_title(f"Distribution des Évaluations", fontsize=18)
    axs[1, 1].set_ylabel("Évaluation", fontsize=14)
    axs[1, 1].set_ylim(0.5, 7.5)
    axs[1, 1].set_yticks(range(0, 8))
    
    # Save the visualization in the "visualizations" folder
    plt.savefig(f'visualizations/visualization_{sound}.png', dpi=300, bbox_inches='tight')
    print(f"Les visualisations pour {sound} ont été sauvegardées dans 'visualizations/visualization_{sound}.png'")
    plt.close()

# Fonction principale
def main():
    df = load_data()
    attractiveness_columns, keyword_columns = define_columns(df)
    results = analyze_sounds(df, attractiveness_columns, keyword_columns)
    display_results(results)
    save_results(results)
    
    # Проверка на пустоту результатов перед визуализацией
    if results:
        # Charger les résultats pour la visualisation
        results_df = pd.read_csv('analysis_results.csv', index_col=0)
        results_df['All Keywords'] = results_df['All Keywords'].apply(safe_eval)
        results_df['Distribution of Ratings'] = results_df['Distribution of Ratings'].apply(safe_eval)
        create_visualizations(results_df)
    else:
        print("Aucun résultat à visualiser.")

if __name__ == "__main__":
    main()