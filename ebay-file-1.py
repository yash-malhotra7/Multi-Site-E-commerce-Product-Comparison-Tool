import requests
import webbrowser
from bs4 import BeautifulSoup
import urllib.parse

query = input("Enter your search query: ")
query_encoded = urllib.parse.quote_plus(query)
url = f"https://www.ebay.com/sch/i.html?_nkw={query_encoded}"

brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
webbrowser.register('brave', None, webbrowser.BackgroundBrowser(brave_path))
webbrowser.get('brave').open(url)

# Get the HTML page of the search results
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the links and prices of the first 10 products
products_list = soup.find_all('li', class_='s-item s-item__pl-on-bottom')[:10]
#price_elements = soup.find_all('span', class_='s-item__price')

# Get the exchange rate of USD to INR
exchange_url = "https://api.exchangerate-api.com/v4/latest/USD"
exchange_response = requests.get(exchange_url)
exchange_data = exchange_response.json()
usd_to_inr = exchange_data['rates']['INR']

product_links = []
product_prices = []

for product in products_list:
    price = product.find('span', {'class':'s-item__price'})
    price_text = price.text
    if not price_text.startswith('$'):
        continue  # skip prices that do not start with the dollar sign
    try:
        price_usd = float(price_text[1:])
    except ValueError:
        continue  # skip prices that cannot be converted to float
    price_inr = round(price_usd * usd_to_inr, 2)  # convert to INR and round to 2 decimal places
    product_link = product.find('a', {'class': 's-item__link'}).get('href')
    print(price_inr)
    print(product_link + "\n")
    product_links.append(product_link)
    product_prices.append(price_inr)
