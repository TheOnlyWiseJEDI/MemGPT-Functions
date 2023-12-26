import requests
import re
import os

docs_dir = os.path.join(os.path.expanduser("~"), "Documents")

def check_movies(self, movie_name: str):
    """
    Get movie information from The Movie Database online. Set heartbeat = True and return all results.
    
    Args:
        movie_name (str):  The name of the movie to search for
        
    Returns:
        str: One or more movie results in plain text
        
    """
    # movie_name = "Firefly"
    base_url = 'https://api.themoviedb.org/3/search/movie?query='
    api_key = "&api_key=YOUR-API-KEY"
    num_results = 3
    
    print(f"Searching the Movie Database for: {movie_name}")
    # Build Url
    url = (base_url + movie_name + api_key)
    
    # Send a GET request to the API
    movie_api_results = requests.get(url)
    
    # Parse the JSON response
    movie_results_json = movie_api_results.json()

    # Limit the results to the desired number (e.g., 3)
    limited_results = movie_results_json.get('results', [])[:num_results]
    
    # Check if the request was successful (status code 200)
    if movie_api_results.status_code == 200:
        
        # Extract JSON content from the response
        results_json = movie_api_results.json()

        # Nested function for cleaning text
        def clean_text(text):
            # Remove all non-alphanumeric characters except for special cases like ‘
            cleaned_text = re.sub(r'[^\w\s‘’]', '', text)
            return cleaned_text

        # Nested function for writing results to text file
        def write_movie_results_to_text_file(limited_results, file):
            global docs_dir
            
            imdb_prefix = "https://www.imdb.com/find/?q="
            imbd_suffix = "&ref_=nv_sr_sm"
            
            for index, result in enumerate(limited_results, start=1):  # <-- Fix here
                file.write(f"Result {index}:\n")
                file.write(f"Title: {clean_text(result.get('title', 'N/A'))}\n")
                file.write(f"Overview: {clean_text(result.get('overview', 'N/A'))}\n")
                file.write(f"Release Date: {clean_text(result.get('release_date', 'N/A'))}\n")
                #file.write(f"Popularity: {clean_text(str(result.get('popularity', 'N/A')))}\n")
                #file.write(f"Vote Average: {clean_text(str(result.get('vote_average', 'N/A')))}\n")
                #file.write(f"Vote Count: {clean_text(str(result.get('vote_count', 'N/A')))}\n")

                #genres = ', '.join(clean_text(str(genre_id)) for genre_id in result.get('genre_ids', []))
                #file.write(f"Genre IDs: {genres}\n")
                
                imdb_url = (imdb_prefix + clean_text(result.get('title', 'N/A')) + imbd_suffix)
                file.write(f"Link: {imdb_url}\n")
                file.write("\n")  # Add a newline between results

        file_path = (docs_dir + '\movie_output.txt')
        
        with open(file_path, 'w', encoding='utf-8') as file:
            write_movie_results_to_text_file(limited_results, file)
            
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
            return file_content    
    else:
        print(f"Failed to fetch movie data. Status code: {movie_api_results.status_code}")


