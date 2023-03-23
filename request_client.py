import time
import requests

ip_address = "http://ip:port"  # Replace with the desired IP address

while True:
    response = requests.get(ip_address)
    # Process the response here if needed
    time.sleep(60)  # Wait for 60 seconds before making the next request