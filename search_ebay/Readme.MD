This function will take a keyword(s) and perform an eBay search and return results to MemGPT.

It requires an eBay production API key which is free. Simply edit the file and replace YOUR-PRODUCTION-API-KEY when you get one.

You will notice that many 'fields' from the JSON results are commented out, this was done to reduce amount of detail returned. Adjust as desired.

This function also writes the results to two  files (.txt and .json) and palces them in the Documents directory for the current Windows user.
The JSON file is created and available for other uses if needed.
The files are over-written on each run.
  
By design the files are created and then used to produce results for MemGpt.

The number of results returned can also be adjusted in the script by setting; num_results.

Updated: 12/27/2023
  The URL's provided by the eBay API are not functional, they lead to 'item not found' on eBay's site so I replaced it with a URL link that leads to the 'search results' page on eBay for the item.
