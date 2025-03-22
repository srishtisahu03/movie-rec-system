import pandas as pd
import numpy as np
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies_data = pd.read_csv('https://raw.githubusercontent.com/srishtisahu03/movie-rec-system/refs/heads/main/movies.csv')

selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']

for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna('')

combined_features = movies_data['genres'] + movies_data['keywords'] + movies_data['tagline'] + movies_data['cast'] + movies_data['director']

vectorizer = TfidfVectorizer()

feature_vectors = vectorizer.fit_transform(combined_features)

similarity = cosine_similarity(feature_vectors)

movie_name = input('Enter a movie name : ')

list_of_all_titles = movies_data['title'].tolist()

def find_best_movie_match(query, title_list):
    query = query.lower()
    
    for title in title_list:
        if title.lower() == query:
            return title
    
    matching_titles = [title for title in title_list 
                      if query in title.lower() or title.lower() in query]
    
    if matching_titles:
        return matching_titles[0]  # first match
    
    query_words = query.split()
    main_words = [word for word in query_words if len(word) > 3]  # Filter out short words
    
    if main_words:
        for main_word in main_words:
            matches = [title for title in title_list if main_word in title.lower()]
            if matches:
                return matches[0]  # first match with the main word
    
    # Fall back to difflib as last resort
    close_matches = difflib.get_close_matches(query, title_list, cutoff=0.4)
    if close_matches:
        return close_matches[0]
    
    return None  # No match 

# best match
closest_match = find_best_movie_match(movie_name, list_of_all_titles)

if closest_match:
    print(f"Finding recommendations based on: {closest_match}")
    
    index_of_the_movie = movies_data[movies_data.title == closest_match]['index'].values[0]
    similarity_score = list(enumerate(similarity[index_of_the_movie]))
    sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True)
    
    print('\nSuggested movies : \n')
    i=1
    for movie in sorted_similar_movies:
        index = movie[0]
        title_from_index = movies_data[movies_data.index==index]['title'].values[0]
        if (i<21):
            print(i, '.', title_from_index)
            i += 1
else:
    
    print(f"No movies similar to '{movie_name}' found. Please try another movie name.")