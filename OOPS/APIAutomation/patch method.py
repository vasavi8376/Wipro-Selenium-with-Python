import requests
try:
    data = {
   "name": "Apple MacBook Pro 16 (Updated Name)"
}
    # make a put request to a api endpoint
    response = requests.patch("https://api.restful-api.dev/objects/ff8081819782e69e019c50cda4686474", json=data)
    print(response)

    # check if tyhe status code is 200 ok
    if response.status_code == 200:
        print("Status code is 200 k")
        # parse the json file
        data = response.json()
        print(data)
    else: print(f"Error: Received status code {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occured: {e}")
