import requests
import json
import html
import re
import os

def search_api(self, query: str):
    """
    Perform an internet search using the Google Custom Search API.  Always set heartbeat = True, and use send_message after running this function to provide the result.

    Args:
        query (str): The search query.
        
    Returns:
        dict: The JSON response from the News API. Five search results.
    """
    num_results = 5
    
    # Google Custom Search API endpoint settings
    api_key='YOUR-API-KEY'
    cx='YOUR-CX-CODE'
    api_url = 'https://www.googleapis.com/customsearch/v1'
    
    # Set up parameters
    params = {
        'key': api_key,
        'cx': cx,
        'q': query,
        'num': num_results,
    }

    try:
        print(f"Launching Google search API with keyword(s): {query}\nsearching at: {api_url}")
        # Make the API request
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse and return the JSON response
        search_results = response.json().get('items', [])
        print(f"Response code: {response.status_code}\n")
        
    except requests.exceptions.RequestException as e:
        print(f"Error making the API request: {e}")
        return None

    def clean_snippet(snippet):
        # Remove non-ASCII characters except periods
        cleaned_snippet = re.sub(r'[^\x00-\x7F.]+', ' ', snippet)
        return cleaned_snippet
        
    def write_results_to_text_file(results, file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            for index, result in enumerate(results, start=1):
                file.write(f"Result {index}:\n")
                file.write(f"Title: {result.get('title', 'N/A')}\n")
                file.write(f"Link: {result.get('link', 'N/A')}\n")

                # Handle multiline snippet
                snippet = result.get('snippet', '')
                decoded_snippet = html.unescape(snippet)
                cleaned_snippet = clean_snippet(decoded_snippet)
                snippet_lines = cleaned_snippet.split('\n')

                file.write("Snippet:")
                for line in snippet_lines:
                    if line.endswith('.'):
                        file.write(f"  {line}\n")
                    else:
                        file.write(f"  {line}.\n")
                
                file.write("\n")  # Add a newline between results                
                
    docs_dir = os.path.join(os.path.expanduser("~"), "Documents")
    file_path = (docs_dir + '\search_results.txt')
    print(file_path)
    write_results_to_text_file(search_results, file_path)
    
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()
        
    return(file_content)



        
