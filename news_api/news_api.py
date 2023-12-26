import requests
import html
import re
import os

num_results = 5
api_key = 'YOUR-API-KEY'
category = "general"

def news_api(self, query: str):
    """
    Search the News API for articles. Set heartbeat = True and return all results.
    
    Args:
        query (str): Keywords to search for
    
    Returns:
        str: Text results of the search   
    """
    print(f"Searching the News API for: {query}")
    
    global num_results
    global api_key
    global category
    
    docs_dir = os.path.join(os.path.expanduser("~"), "Documents")
    
    def clean_snippet(snippet):
        # Remove non-ASCII characters except periods
        cleaned_snippet = re.sub(r'[^\x00-\x7F.]+', ' ', snippet)
        return cleaned_snippet

    def write_results_to_text_file(results, file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            for index, result in enumerate(results.get('articles', []), start=1):
                file.write(f"Result {index}:\n")
                file.write(f"Title: {result.get('title', 'N/A')}\n")
                file.write(f"Description: {result.get('description', 'N/A')}\n")
                file.write(f"URL: {result.get('url', 'N/A')}\n")
                file.write(f"Published At: {result.get('publishedAt', 'N/A')}\n")

                # Handle multiline description
                description = result.get('description', '')
                decoded_description = html.unescape(description)
                cleaned_description = clean_snippet(decoded_description)
                description_lines = cleaned_description.split('\n')

                file.write("\n")  # Add a newline between results            
            
    base_url = 'https://newsapi.org/v2/top-headlines'
    
    params = {
        'apiKey': api_key,
        'country': "us",
        'category': category,
        'results': num_results,
        'q': query,
    }

    print(f"Launching News API searching for: {query}\nSearching at: {base_url}")
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        print(f"Response code: {response.status_code}\n")
        news_api_results = response.json()
        #print(news_api_results)
        
        file_path = (docs_dir + 'news_output.txt')
        write_results_to_text_file(news_api_results, file_path)
        
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
        
        return file_content
    else:
        print(f"Failed code: {response.status_code}\n")
        # Handle error cases here

    
