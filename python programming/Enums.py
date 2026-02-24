fruits = ["orange", "cherry", "kiwi"]
for index,fruit in enumerate(fruits):
    print(index, fruit)

#enumerate with start value changed
for index,fruit in enumerate(fruits, start=1):
    print(index, fruit)

#enumerate with strings
word = "python"
for i, ch in enumerate(word):
    print(i, ch)

#enumerate with tuples
fruits = ("orange", "cherry", "kiwi")
for index,fruit in enumerate(fruits):
    print(index, fruit)

#real time examples
test_cases = ["login", "signup", "checkout"]
for case_no, test in enumerate(test_cases, start =1):
    print(f"Executing Testcase{case_no}: {test}")

#accessing the enumerates
a = ['god', 'is', 'great']
b = enumerate(a)
nxt_val = next(b)
print(nxt_val)

#duplicates detection of enumerates
characters = ["Vasavi", "Bunny", "Vivek", "Megha", "Vasu",
              "Vasavi", "Bunny", "Vivek", "Megha", "Vasu",
              "Vasavi", "Bunny", "Vivek", "Megha", "Vasu"]
character_map = {character: [] for character in set(characters)}
for index, character in enumerate(characters):
    character_map[character].append(index)

print(character_map)

