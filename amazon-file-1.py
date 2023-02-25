import webbrowser
import os
import urllib.request
from bs4 import BeautifulSoup
import random

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.57',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
]

user_agent = random.choice(user_agents)

headers = {
    'User-Agent': user_agent
}

input_str = input("Enter a search term: ")
input_str = input_str.replace(" ", "+")

url = f"https://www.amazon.in/s?k={input_str}"
brave_path = "C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"  # Replace with the path to your Chrome executable

# Set the BROWSER environment variable to the path of the Chrome executable
os.environ["BROWSER"] = brave_path

webbrowser.open(url)

# Send a request to the Amazon URL and get the HTML response
req = urllib.request.Request(url, headers=headers)
html = urllib.request.urlopen(req).read()

# Parse the HTML response using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find the first product link in the search results
products = soup.find_all('div', {'data-component-type': 's-search-result'})[:10]


product_links = []
# Find the price of the product
for product in products:
    price = product.find('span', {'class': 'a-offscreen'})
    print('The price of the product is:', price.text.strip())
    product_link = product.find('a', {'class': 'a-link-normal s-no-outline'}).get('href')
    product_link = "https://www.amazon.in" + product_link
    product_links.append(product_link)
