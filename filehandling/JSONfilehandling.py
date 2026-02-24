import json

with open("C://Users//ansur//PycharmProjects//PythonProject//Dataformats//employee.json",'r')as file:
    data=json.load(file)

#read the json file
print(data)
print(data["name"])

with open("C://Users//ansur//PycharmProjects//PythonProject//Dataformats//nested.json",'r')as file:
    data = json.load(file)

email =data["user"]["profile"]["email"]
print(email)

#writing the json file
data ={
  "name": "Harsha",
  "role": "Tester",
  "experience": 5,
  "skills": ["Python", "Automation", "API"]
}

with open("C://Users//ansur//PycharmProjects//PythonProject//Dataformats//writejson.json",'w')as file:
            json.dump(data,file)

#update or modify
#read
#modify
#write it back
try:
    file = open("data.txt", "r")   # file may not exist
    content = file.read()
    print(content)
    file.close()

except FileNotFoundError:
    print("Error: File not found!")

with open("C://Users//ansur//PycharmProjects//PythonProject//Dataformats//updatejson.json", 'r') as file:
    data = json.load(file)

data["experience"] = 6

with open("C://Users//ansur//PycharmProjects//PythonProject//Dataformats//updatejson.json", 'w') as file:
    json.dump(data, file, indent=4)











