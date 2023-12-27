import requests
import json
import os

docs_dir = os.path.join(os.path.expanduser("~"), "Documents")

def search_ebay(self, keywords_to_search: str):
    
    """
    Search Ebay using keyword(s) for an item. Set heartbeat = True when running this function and send_message ALL of the results.
    
    Args:
        keywords_to_search (str): Keyword or words to search for
        
    Returns:
        str: JSON Formatted list
    """

    global docs_dir
    keywords = keywords_to_search
    
    def format_ebay_item(item):
        return (
            #f"Item ID: {item['itemId'][0]}\n"
            f"Title: {item['title'][0]}\n"
            #f"Global ID: {item['globalId'][0]}\n"
            #f"Category ID: {item['primaryCategory'][0]['categoryId'][0]}\n"
            #f"Category: {item['primaryCategory'][0]['categoryName'][0]}\n"
            #f"Gallery URL: {item['galleryURL'][0]}\n"
            #f"URL: {item['viewItemURL'][0]}\n"
            #f"AutoPay: {item['autoPay'][0]}\n"
            #f"Postal Code: {item['postalCode'][0]}\n"
            f"Location: {item['location'][0]}\n"
            #f"Country: {item['country'][0]}\n"
            f"Shipping: {item['shippingInfo'][0]['shippingServiceCost'][0]['__value__']}\n"
            f"Ship Type: {item['shippingInfo'][0]['shippingType'][0]}\n"
            #f"Ship To Locations: {', '.join(item['shippingInfo'][0]['shipToLocations'])}\n"
            #f"Expedited Shipping: {item['shippingInfo'][0]['expeditedShipping'][0]}\n"
            #f"One Day Shipping Available: {item['shippingInfo'][0]['oneDayShippingAvailable'][0]}\n"
            #f"Handling Time: {item['shippingInfo'][0]['handlingTime'][0]}\n"
            #f"Current Price (USD): {item['sellingStatus'][0]['currentPrice'][0]['__value__']}\n"
            f"Price: {item['sellingStatus'][0]['convertedCurrentPrice'][0]['__value__']}\n"
            #f"Selling State: {item['sellingStatus'][0]['sellingState'][0]}\n"
            #f"Time Left: {item['sellingStatus'][0]['timeLeft'][0]}\n"
            #f"Best Offer Enabled: {item['listingInfo'][0]['bestOfferEnabled'][0]}\n"
            f"Buy It Now: {item['listingInfo'][0]['buyItNowAvailable'][0]}\n"
            #f"Start Time: {item['listingInfo'][0]['startTime'][0]}\n"
            #f"End Time: {item['listingInfo'][0]['endTime'][0]}\n"
            #f"Listing Type: {item['listingInfo'][0]['listingType'][0]}\n"
            #f"Gift: {item['listingInfo'][0]['gift'][0]}\n"
            #f"Returns Accepted: {item['returnsAccepted'][0]}\n"
            #f"Condition ID: {item['condition'][0]['conditionId'][0]}\n"
            f"Condition: {item['condition'][0]['conditionDisplayName'][0]}\n"
            #f"Is Multi-Variation Listing: {item['isMultiVariationListing'][0]}\n"
            #f"Top Rated Listing: {item['topRatedListing'][0]}\n"
            )

    def convert_to_plain_text(item):
        """
        Convert eBay API item details to plain text format.
        """
        return format_ebay_item(item) + "\n"

    def ebay_api_search(keywords):
        global docs_dir
        num_results=3
    
        print(f"Searching eBay for: {keywords}")
        
        # Replace 'YourProductionAppID' with your actual eBay developer application ID
        app_id = 'RonJohns-SearchAP-PRD-3834dfaa0-ff4831a9'
        
        # URL for the eBay Finding API
        url = f'https://svcs.ebay.com/services/search/FindingService/v1?' \
              f'OPERATION-NAME=findItemsAdvanced&SERVICE-VERSION=1.0.0&SECURITY-APPNAME={app_id}' \
              f'&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD&keywords={keywords}' \
              f'&itemFilter(0).name=Title&itemFilter(0).value={keywords}' \
              f'&itemFilter(1).name=Description&itemFilter(1).value={keywords}' \
              f'&paginationInput.entriesPerPage={num_results}'

        # Make the API call
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            json_response = response.json()

            # Write results to plain text file
            with open(docs_dir + "\\" + "ebay_results.txt", 'w', encoding='utf-8') as text_file:
                for item in json_response.get('findItemsAdvancedResponse', [])[0].get('searchResult', [])[0].get('item', []):
                    text_file.write(convert_to_plain_text(item))
            
            # Build a url for the ebay results page and append it to the file
            with open(docs_dir + "\\" + "ebay_results.txt", 'a', encoding='utf-8') as text_file:
                results_url = (f"https://www.ebay.com/sch/i.html?_nkw={keywords}&_ddo=1&_ipg=1&_pgn=1")
                text_file.write(f"URL: {results_url}\n")
            
            # Write results to JSON file
            with open(docs_dir + 'ebay_results.json', 'w', encoding='utf-8') as json_file:
                json.dump(json_response, json_file, indent=2)

            # Customize the return statement based on the fields you want to include
            return {
                'title': item.get('title', ['N/A'])[0],
                'item_url': item.get('viewItemURL', ['N/A'])[0],
                'location': item.get('location', ['N/A'])[0],
                'current_price': item.get('sellingStatus', [{}])[0].get('currentPrice', [{}])[0].get('__value__', 'N/A')
            }

        else:
            # Print an error message if the request was not successful
            print(f"Error: {response.status_code}")
            return None    

    results = ebay_api_search(keywords)
    
    file_path = (docs_dir + "\\" + "ebay_results.txt")

    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()
        
    # Return either 'results' (JSON) or 'file_content' (text file output)
    return(file_content)

