#subprocess module
#execute external system commands
#interact with os processess
#capture output, error and return codes
#control the process execution
#run the os level commands - linux, macos, windows
#subprocess.run() - runs command and wait
#subprocess.Papen() - run process asynchronusly
#subprocess.PIPE - capture the output
#subprocess.CompleteProcess - result
#subprocess.TimeoutExpired - Time outexpection
#subprocess.calledProcessError -command failure
import subprocess
result = subprocess.run("dir" , shell = True , capture_output=True, text = True)
print(result)

result = subprocess.run("ipconfig" , shell = True , capture_output=True, text = True)
print(result)

result = subprocess.run("python --version" , shell = True , capture_output=True, text = True)
print(result.stdout)#captures the output
print(result.stderr)