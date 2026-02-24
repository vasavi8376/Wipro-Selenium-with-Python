from bs4 import BeautifulSoup

html = '''
<html>
<head><title>My Page</title></head>
<body>
<h1>Welcome</h1>
<p>This is a paragraph.</p>
<a href="https://google.com">Google</a>
<h2>Subtitle</h2>
<b>Bold Text</b>
<img src="image.png" alt="Sample">
<table>
<tr><td>Name</td><td>Age</td></tr>
<tr><td>John</td><td>25</td></tr>
</table>

</body>
</html>
'''

soup = BeautifulSoup(html, "html.parser")

# Extract Title and h1
print(soup.title.text)
print(soup.h1.text)

# Extract All Paragraphs
para = soup.find_all("p")
for p in para:
    print(p.text)

# Extract All Links and Count
links  = soup.find_all("a")
print("Total links:", len(links))

for link in links:
    print(link.text)

# Extract Attributes
link1 = soup.find("a")
print(link1.get("href"))

# Extract First h2
h2 = soup.find("h1")
print(h2.text)

# Extract Bold Text
bold = soup.find("b")
print(bold.text)

# Extract All href Values
links3 = soup.find_all("a")
for link3 in links3:
    print(link3["href"])

# Get All Text Without Tags
print(soup.get_text())

# Extract Title from Website
import requests

response = requests.get("https://google.com")
soup = BeautifulSoup(response.text, "html.parser")
print(soup.title.text)

# Extract All Headings
headings = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])

for heading in headings:
    print(heading.text)

# Extract Table Data
rows = soup.find_all("tr")

for row in rows:
    columns = row.find_all("td")
    for col in columns:
        print(col.text)

# Extract Images
images = soup.find_all("img")

for img in images:
    print(img.get("src"))