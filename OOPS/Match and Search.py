#match - match the exact sequence
#o/p match object - matched sequence and span() - start and end index
#checks for a match only at the beginning of the string.
#returns a match object if found, else no

import re
text = "hello world"
result = re.match("hello", text)
print(result)
#using pattern
test_str = "123566778abcghhhjhjabcABC"
pattern = re.compile("123")
#re.finditer() finds all non overlapping matches of a pattern in a stirng
#and returns an iterator of match objects(not a list)
matches = pattern.finditer(test_str)
for match in matches:
    print(match)
#search operation searches the entire string
#returns the first occurrence

text = "python of powerful"
result = re.search("powerful", text)
print(result)

#search - search the entire string - find the occurrneces
#match - begginning only - validate the formats
#raw string - it is used for including the special characters
a = r"\tHello"
print(a)

#match() - determine if the RE matches at the beginning of the string.
#search() - scan through a string, looking for any location where this RE matches
#finditer() - find all substrings where the RE matches and returns them as a iterator
#findall() - find all the strings where the re matches and return a list
#find(all)
my_string = "abc123ABC123abc"
pattern = re.compile(r'123')
matches = pattern.findall(my_string)

for match in matches:
    print(match)

#methods on match
#group() - return the string matched by the RE
#start() - return the starting position of the match
#end() - return the ending position of the match
#span() - return a tuple containing the (start, end) positions of the match

test_string = "123abc456789abc123ABC"
pattern = re.compile(r'abc')
matches = pattern.finditer(test_string)

for match in matches:
    print(match)
    print(match.span(), match.start(), match.end())
    print(match.group())


#regular expressions
#pattern meaning
#abc matches exact text
#[abc] a or b or c
#[a-z]  lowercase letters
#[0-9] Digits
#a b
#  any single character
#abc - matches exact text
#Match exact "abc" where ever it is appearing
text = "I like abc and abcde"
result = re.findall("[a-z]", text)
print(result)

#[abc] a or b or c - matches any one of the character
#matches single characters: a or b or c
text = "apple banana cat"
result = re.findall("[abc]", text)
print(result)

#[a-z] lowercase letters
text = "I like abc and ABCGHJHJH"
result = re.findall("[a-z]", text)
print(result)

#[0 - 9] digits
text = "I like abc and 123455ABCGHJHJH"
result = re.findall("[0-9]", text)
print(result)

#'a b'
text = "cat bat rat mat"
result = re.findall("cat|bat", text)
print(result)
#matches either "cat" or "rat"

#any single character
text = "cat bat rat bob"
result = re.findall("c.t", text)
print(result)

#special characters
'''
special sequences begin with a backslash\.
\d digit (0-9)
\D non digit \D
\w word char (a-z, A-Z, O-9) \w+
\W non word char \W
\s whitespace \s
\S non white space \S
\b word boundary \bcat\b
\B not a word boundary \Bcat
'''
#\d digit (0-9)
print (re.findall(r"\d", "order 123 costs 450"))
#\D non digit \D
print (re.findall(r"\D", "order 123 costs 450"))
#\w word char (a-z, A-Z, O-9) \w
text = "Python_3 version"
result = re.findall(r"\w", text)
print(result)
#\W non word char \W
#matches anything that is not a word character.
text = "Hello@123!"
result = re.findall(r"\W", text)
print(result)
#\s whitespace, tabs and newline \s
text = "Hello World\nPython"
result = re.findall(r"\s", text)
print(result)
#\S non white space \S - matches anything that is NOT space, tab, newline
text = "Hi There"
result = re.findall(r"\S", text)
print(result)
#\b word boundary \bcat\b - matche position at start or end of a word
text = "cat scatter catalog"
result = re.findall(r"cat\b", text)
print(result)
#\B not a word boundary \Bcat - methods when pattern is NoT at word boundary
text = "cat scatter catalog"
result = re.findall(r"cat\B", text)
print(result)

#meta characters have special meaning in regix
#meta character meaning - any character
'''
start of string
end of string
o or more
1 or more
{n} exactly n times
{n,m} between n and m
[] character set
() grouping
'''
#srat of string
text = "Python is easy"
print(re.findall(r"^Python", text))

#end of string
text = "Python is easy"
print(re.findall(r"easy$", text))

# 0 or more
text = "ab abb a n"
print(re.findall(r"ab*", text))
# 1 or more
text = "ab abb a n"
print(re.findall(r"ab+", text))
#0 or 1
text = "color colour colr"
print(re.findall(r"colou?r", text))
#{n} exactly n times
text = "111 22 3333 68777"
print(re.findall(r"\d{3}", text))
#{n,} n or more times
text = "1 22 333 4444"
print(re.findall(r"\d{3}", text))
#{n, m} between n and m
text = "1 22 333 4444"
print(re.findall(r"\d{2,3}", text))
#character set
text = "apple banana cat"
print(re.findall(r"[abc]", text))
# grouping
text = "2026-02-11"
result = re.findall(r"(\d{4})-(\d{2})-(\d{2})", text)
print(result)

#Regular expression modifiers
'''
Modifier short purpose
re.ignorecase re.I case insensitive matching
re.multiline -re.M - ^ and $ match each line
re.DOTALL - re.S - matches new line
re.verbose - re.X - write readable regex with comments
re.ASCII - re.A - ASCII only matching
re,Debug -Debug Pattern
'''
#re.ignore case re.I case insensitive matching
text = "Python"
print(re.search("python", text, re.I))
#re,multiline re.M  ^ & $ match each line
text = "Hello\nPython"
print(re.findall("^Python", text, re.M))
#re.DoTALL re.S, matches new line
text = "Hello\nWorld"
print(re.search("Hello.*World", text, re.S))
#re.VERBOSE re.x - write readble regex with comments - make it more readable


#assertitions - validating the output or checking certain condition
'''
start of the string
end of the string
not word boundary
positive lookahead
negative lookahead


'''
#positive lookahead
text = "user1 admin2 test"
print(re.findall(r"\w+(?=\d)", text))
#negative lookahead
text = "user1 admin test2"
print(re.findall(r"\w+(?!\d)", text))
#positive lookbehind
text = "Price -500"
print(re.findall(r"(?<=-)\d+", text))
#negative lookbehind
text = "500 - 300"
print(re.findall(r"(?<!-)\d+", text))




