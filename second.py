import requests
import logging
import time

logging.basicConfig(
    filename="logs.txt", 
    level=logging.DEBUG,
    style="{",
    format="{asctime} {levelname:<8} {message}"
)

while True:
    try:
        response = requests.get("http://127.0.0.1:8080/health")
        break
    except requests.exceptions.RequestException as error:
        logging.error(error)
        time.sleep(60)
        
        
print("-------------------------------")
