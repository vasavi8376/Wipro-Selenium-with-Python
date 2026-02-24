#Destructors - when we want to destroy the object
#post condition - closing of the browser, db connection closing, reasing of certain resources
#cleanup operations
#for proper memory usage destructors should be used
# when db connection has to be closed
# free the memory(garbage collection)which is automatically called
#destructor runs
class Desct:
    def __init__(self):
        print("object created")
    def __del__(self):
        print("closing the db connection")

a = Desct()
print("End the Program")

#destructor in fils handling
class FileHandler:
    def __init__(self, filename):
        self.file = open (filename, 'w')
        print("File is Opened")
    def readfile(self, filename):
        print("Reading the File")
    def __del__(self):
        self.file.close()
        print("File Closed")
f = FileHandler("test.txt")
f.readfile("test.txt")
del f