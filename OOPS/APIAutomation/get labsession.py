import requests
#get all objects
try:
    # make a get request to be api endpoint
    response= requests.get("https://api.restful-api.dev/objects")
    print(response)

#check if type status code is 200 ok
    if response.status_code == 200:
        print("Status code is 200 ok")

        data = response.json()
        print(data)

    else: print(f"Error : Recieved status code{response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occured:{e}")

#get single object
try:
    # make a get request to be api endpoint
    response= requests.get("https://api.restful-api.dev/objects/7")
    print(response)

#check if type status code is 200 ok
    if response.status_code == 200:
        print("Status code is 200 ok")

        data = response.json()
        print(data)

    else: print(f"Error : Recieved status code{response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occured:{e}")

#get object with id

try:
    # make a get request to be api endpoint
    response= requests.get("https://api.restful-api.dev/objects?id=3&id=5&id=10")
    print(response)

#check if type status code is 200 ok
    if response.status_code == 200:
        print("Status code is 200 ok")

        data = response.json()
        print(data)

    else: print(f"Error : Recieved status code{response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occured:{e}")

