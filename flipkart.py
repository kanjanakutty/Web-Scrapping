from bs4 import BeautifulSoup
import requests
import pandas as pd

URL = "https://www.amazon.in/gp/bestsellers/computers/ref=zg_bsomputers_sm"

headers=({'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36", 'Accept-Language':'en-US, en;q=0.5'})

webpage = requests.get(URL,headers)

soup = BeautifulSoup(webpage.content, "html.parser")

links = soup.find_all("a", attrs={'class':'a-link-normal'})
print(links)

link = links[0].get("href")
print(link)

product_list="https://www.amazon.in/"+link
print(product_list)

new_product=requests.get(product_list)
print(new_product)

new_soup = BeautifulSoup(new_product.content, "html.parser")

title = soup.find("span", attrs={'id':'productTitle'}).text.strip()

print(title)

price = soup.find("span", attrs={'class':'a-price-whole'})

ratings = soup.find("span", attrs={'class':'a-size-base a-color-base'})
