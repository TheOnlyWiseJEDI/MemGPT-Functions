import requests
import json

api_key = "YOUR-SUPER-LONG-API-KEY-HERE"
autoremote_url = f"https://autoremotejoaomgcd.appspot.com/sendnotification?key={api_key}&text="

def send_notification(self, message: str):

    """
    Sends a text notification to the users phone when they are away. Set heartbeat = True when running this function.
    
    Args:
        message (str): The message to be sent to cell phone 
        
    Returns:
        str: HTTP GET result, '200' if successful
        
    """
    print("Launching notification process..")
    packaged_message = f"{autoremote_url}{message}&sender=MemGPT"
    
    #printd(f"Sending notification:\n\n{message} to autoremote")
    
    result = requests.get(packaged_message)
    
    #printd(result)
    
    return f"Message sent with result:{result}"
