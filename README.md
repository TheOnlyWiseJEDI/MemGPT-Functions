# MemGPT-Functions
Python Functions for MemGPT

These functions created for use with MemGPT are designed with the Windows operating system in mind. 
Mostly the os dependency is file-system related and they can be edited to work on linux and Mac fairly easily.

The search related functions such as 'check_movies', 'search_api', 'news_api' and 'search_ebay' each return results that have url's. 

With 'send_to_chrome' installed, you can ask the AI to open any of the results in the default browser. 
'send_to_chrome' is probably Windows specific so it will be necessary to write a function for other os's for this.
For windows it's a tiny super basic and easy to make function.

For each of the functions you may need an API KEY.
All API related are are based on free API's except the rocket_launch function.

