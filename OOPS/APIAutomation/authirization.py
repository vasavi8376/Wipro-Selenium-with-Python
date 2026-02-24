import requests
from requests.auth import HTTPBasicAuth

try:

    headers = {
        "User-agent": "Myapp/1.0" ,
        "Accept": "application/json"
    }
    # make a get request to be api endpoint
    response= requests.get("https://videogamedb.uk:443/api/v2/videogame", auth=HTTPBasicAuth('username', 'password'), timeout=5, headers= headers)
    print(response)

#check if type status code is 200 ok
    if response.status_code == 200:
        print("Status code is 200 ok")

        data = response.json()
        print(data)

    else: print(f"Error : Recieved status code{response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occured:{e}")