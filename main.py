import requests
import lxml
from bs4 import BeautifulSoup

session = requests.Session()
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

data = input("Input url categories ")
for i in range(1, 10):
    print(f"PAGE -> {i}")
    url = f"{data}p-{i}/"
    response = session.get(url, headers=header)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")
        all_products = soup.find('div', class_="catalog-grid ng-star-inserted")
        products = all_products.find_all('div', class_="goods-tile__content")
        discount = all_products.find_all('div', class_="goods-tile__price-currency currency")

        for j in range(len(products)):
            try:
                title_ = products[j].find("a", class_="catalog-grid ng-star-inserted").text
                price = products[j].find("div", class_="goods-tile__content").text
                discount = products[j].find("div", class_="goods-tile__price-currency currency").text
                with open("products.txt", "a", encoding="UTF-8") as file:
                    file.write(f"{title_}  {price}  {discount}\n")
                print(title_, price, discount)
            except:
                print(f"{title_} - знижки немає")
