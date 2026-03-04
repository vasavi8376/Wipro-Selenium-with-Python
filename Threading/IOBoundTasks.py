import time
# IO bound tasks
'''

An I/O-bound task is a task where:

The program waits for data from external resources

CPU is mostly idle while waiting

Performance is limited by disk, network, or database speed

Examples of external resources:

Files

Network requests

Databases

APIs

User input

'''

# Example - without using the threading concept
def task():
    print("Task started")
    time.sleep(3)
    print("Task completed")
task()
task()

#total time taken 6 seconds
import threading
# multiple tasks concurrently within a single process.
# Threads share the same memory space of the process.
# This allows faster communication between them.

def task():
    print("Task started")
    time.sleep(3)
    print("Task completed")

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)

t1.start()
t2.start()

t1.join()
t2.join()

#fetch the api details

def fetch_data(api_name):
    print(f"fetching from {api_name}")
    time.sleep(2)
    print(f"completed {api_name}")

apis = ["API1", "API2", "API3"]
threads = []

for api in apis:
    t = threading.Thread(target=fetch_data, args=(api,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()

print("All the API calls completed")

#file reading
def read_file(file_name):
    with open(file_name, "r") as f:
        data = f.read()
        print(f"{file_name} read completed")

files = ["file1.txt", "file2.txt"]
for file in files:
    t = threading.Thread(target=read_file, args=(file,))
    t.start()

for t in threads:
    t.join()


