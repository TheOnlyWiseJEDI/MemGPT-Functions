import subprocess

def ping_ip(self, ip_address: str):
    
    """
    Performs a network ping for a given IP address. After running this function, you should always run send_message to tell the user the result. Always set heartbeat = true
    
    Args:
        ip_address (str): The ip address to ping

    Returns:
        str: Ping results
        
    
    """
    try:
        print(f"\nLaunching Ping process for target ip: {ip_address}\n")
        # Run the ping command
        result = subprocess.run(["ping ", ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, timeout=10)

        # Check the return code to see if the ping was successful
        if result.returncode == 0:
            return f"Ping to {ip_address} was successful:\n{result.stdout}"
        else:
            return f"Ping to {ip_address} failed:\n{result.stderr}"

    except subprocess.TimeoutExpired:
        return f"Timeout expired while trying to ping {ip_address}"

