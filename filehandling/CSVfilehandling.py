import csv

#reading the file
with open("C://Users//ansur//PycharmProjects//PythonProject//Dataformats//data.csv",'r')as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#writing
with open("C://Users//ansur//PycharmProjects//PythonProject//Dataformats//writecsv.csv","w",newline="")as file:
    writer =csv.writer(file)
    writer.writerow(["id","name","marks"])
    writer.writerow([1, "Rahul", 85])
    writer.writerow([2, "Anita", 90])

#appennd
with open("C://Users//ansur//PycharmProjects//PythonProject//Dataformats//data.csv","a",newline="")as file:
    writer =csv.writer(file)
    writer.writerow([3,"kiran",88])


