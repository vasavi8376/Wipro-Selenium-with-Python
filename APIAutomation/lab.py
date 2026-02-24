#to get only username and email
import requests
import json
from requests.exceptions import Timeout
try:
    response = requests.get("https://jsonplaceholder.typicode.com/users")

    if response.status_code == 200:
        print("Status code is 200 OK")

        data = response.json()

        for user in data:
            print(f"Name: {user['name']}, Email: {user['email']}")

    else:
        print(f"Error: Received status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")

#Send a GET request with query parameter userId=2 and print number of posts returned.


try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts",params={"userId": 2})

    if response.status_code == 200:
        print("Status code is 200 OK")

        data = response.json()
        print(f"Number of posts returned: {len(data)}")

    else:
        print(f"Error: Received status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
#POST request to create a new resource and verify status code 201.

try:
    # Data to send in POST request
    data = {
        "title": "New Post",
        "body": "This is a new post created using POST request.",
        "userId": 1
    }

    # Send POST request
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=user)

    # Check if status code is 201 Created
    if response.status_code == 201:
        print("Status code is 201 Created")

        data = response.json()
        print("Response Data:", data)

    else:
        print(f"Error: Received status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")

#response status code is not 200 and raise an exception.
print("\n5️ Status check")
response = requests.get("https://jsonplaceholder.typicode.com/users")

if response.status_code != 200:
    raise Exception(f"Request failed: {response.status_code}")

print("Status code is 200")
#Fetch all users and print usernames in uppercase
try:
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    response.raise_for_status()

    users = response.json()
    for user in users:
        print(user["username"].upper())

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")

#Implement timeout handling (2 seconds) and catch Timeout exception
try:
    response = requests.get("https://jsonplaceholder.typicode.com/users",timeout=2)
    print("Request successful:", response.status_code)

except Timeout:
    print("Request timed out!")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
#Use Session object to send multiple requests and demonstrate cookie persistence
session = requests.Session()
# First request sets a cookie
session.get("https://httpbin.org/cookies/set?mycookie=testvalue")
# Second request retrieves the cookies
response = session.get("https://httpbin.org/cookies")
print("Cookies stored in session:", response.json())

#Upload a file using requests and print server response
url = "https://httpbin.org/post"
with open("test.txt", "w") as f:
    f.write("This is a test file for uploading.\n")
# Open a file in binary mode
with open("test.txt", "rb") as f:
    files = {"file": f}
    response = requests.post(url, files=files)

print("Server response:", response.json())

#Fetch posts and save response JSON into a file named posts.json

try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    response.raise_for_status()

    posts = response.json()
    with open("posts.json", "w") as f:
        json.dump(posts, f, indent=4)

    print("Posts saved to posts.json")

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")



