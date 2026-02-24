import requests

try:
    # make a get request to be api endpoint
    response= requests.get("https://videogamedb.uk:443/api/v2/videogame")
    print(response)

#check if type status code is 200 ok
    if response.status_code == 200:
        print("Status code is 200 ok")

        data = response.json()
        print(data)

    else: print(f"Error : Recieved status code{response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occured:{e}")