import requests
import time
import random

# Replace this with your Render app URL
URL = "https://simple-2-2qt8.onrender.com"

while True:
    try:
        r = requests.get(URL, timeout=10)
        print("Ping:", r.status_code)
    except Exception as e:
        print("Error:", e)

    wait = random.randint(25,40)
    print("Next ping in", wait, "seconds")
    time.sleep(wait)
