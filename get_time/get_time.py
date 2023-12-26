import ntplib
from datetime import datetime, timedelta

def get_time(self):
    """
    Gets the current time for the internet. Set heartbeat = True when running this function.
    
    Args:
        None required
    
    Returns:
        str: The time in text format.
    """
    
    print("Checking time.nist.gov for the current date and time..")
    # Define the NTP server (time.nist.gov)
    ntp_server = 'time.nist.gov'

    # Create an NTP client
    ntp_client = ntplib.NTPClient()

    try:
        # Query the NTP server for the current time
        response = ntp_client.request(ntp_server)

        # Convert NTP timestamp to a datetime object
        ntp_time = datetime.utcfromtimestamp(response.tx_time)
        
        # Adjust for Eastern Standard Time (EST) by subtracting 5 hours
        est_time = ntp_time - timedelta(hours=5)
        
        time_now = (f"{est_time.strftime('%m-%d-%Y %I:%M:%S %p')}")
        #time_now = (f"{est_time.strftime('%I:%M:%S %p')}")
        
        #print(time_now)
        return time_now

    except Exception as e:
        return f"Error: {e}"
