import requests
from bs4 import BeautifulSoup


# 1️ Small HTML string parsing

html_doc = """
<html>
  <head><title>Test Page</title></head>
  <body>
    <h1>Welcome</h1>
    <p>This is a paragraph.</p>
    <a href="https://example.com">Click here</a>

    <article class="product">
        <h2>Book Name</h2>
        <p class="price">$20</p>
        <p class="rating">4 stars</p>
        <p class="availability">In stock</p>
        <img src="image1.jpg">
    </article>
  </body>
</html>
"""

# Parse HTML
soup = BeautifulSoup(html_doc, "html.parser")


# 2️ Extract title, h1, paragraph
print("Title:", soup.title.text)
print("H1:", soup.h1.text)
print("Paragraph:", soup.p.text)


# 3️ Find first <a> tag & href

first_link = soup.find("a")
print("First link href:", first_link.get("href"))


# 4️ Prettify HTML

print("\nFormatted HTML:")
print(soup.prettify())


# 5️ find() vs find_all()

print("\nUsing find():")
print(soup.find("p"))   # first paragraph only

print("\nUsing find_all():")
print(soup.find_all("p"))  # all paragraphs


# 6️ Extract product details

product = soup.find("article", class_="product")

name = product.find("h2").text
price = product.find("p", class_="price").text
rating = product.find("p", class_="rating").text
availability = product.find("p", class_="availability").text

print("\nProduct Details:")
print("Name:", name)
print("Price:", price)
print("Rating:", rating)
print("Availability:", availability)


# 7 Extract all image URLs

images = soup.find_all("img")

print("\nImage URLs:")
for img in images:
    print(img.get("src"))