# scraper.py
import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')

# For commits
# New commit for push to the GitHub
for quote in quotes:
    print(quote.text)
