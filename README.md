# MemGPT-Functions
Python Functions for MemGPT

These functions created for use with MemGPT are designed with the Windows operating system in mind. 
Mostly the os dependency is file-system related and they can be edited to work on linux and Mac fairly easily.

The search related functions such as 'check_movies', 'search_api', 'news_api' and 'search_ebay' each return results that have url's.
(note: I have noticed that the model I use (openhermes) likes to summarize the results and hide the urls, but they exist and asking for one of the results to be opened in the browser still works.) 

With 'send_to_chrome' installed, you can ask the AI to open any of the results in the default browser. 
'send_to_chrome' is probably Windows specific so it will be necessary to write a function for other os's for this.
For windows it's a tiny super basic and easy to make function.

For each of the functions you may need an API KEY.

All that are API related are are based on free API's except the rocket_launch function.

Change updates:
12_26_2023 Corrected path issue for generated files made by 'search_pi', 'search_ebay', 'check_movies' & 'launch_schedule'.
  (Files are saved in the Documents directory of the current Windows user.)

12/27/2023 Updated search_ebay; The URL's provided by the eBay API are not functional, they lead to 'item not found' on eBay's site so I replaced it with a URL link that leads to the 'search results' page on eBay for the original 'keyword(s)'.

