nums = [1, 2, 3, 4, 5]
it = iter(nums)
for num in it:
    print(num)

def generate_numbers(n):
    for i in range(1, n + 1):
        yield i
for i in generate_numbers(5):
    print(i)

def even_numbers(n):
    for i in range(2, n + 1, 2):
        yield i
for num in even_numbers(10):
    print(num)

def read_file(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()
for line in read_file("C://Users//WINDOW 11//PycharmProjects//PythonAdvancedProgramming//Dataframes//employees.json"):
    print(line)

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
for num in fibonacci(7):
    print(num)


def retry_attempts(max_retries=3):
    for attempt in range(1, max_retries + 1):
        yield f"Attempt {attempt}"
for attempt in retry_attempts():
    print(attempt)


