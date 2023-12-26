import webbrowser

def send_to_chrome(self, url: str):
    """
    Send a URL to the Chrome Browser
    
    Args:
        url: (str)  The URL to send to Chrome
        
    Returns:
        str: Reply confirming success
    """

    print(f"Sending URL to Chrome: {url}")

    webbrowser.open(url) 

    return "Success! Browser process launched."
