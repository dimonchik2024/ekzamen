import requests
import lxml
from bs4 import BeautifulSoup

session = requests.Session()
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

data = "https://rozetka.com.ua/ua/shurupoverty-i-elektrootvertki/c152499/"
for i in range(1, 10):
    print(f"PAGE -> {i}")
    url = f"{data}page={i}/"
    response = session.get(url, headers=header)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")
        all_products = soup.find('ul', class_="catalog-grid ng-star-inserted")
        products = all_products.find_all('div', class_="goods-tile__content")
        for j in range(len(products)):
            try:
                title_ = products[j].find("span", class_="goods-tile__title").text
                price = products[j].find("div", class_="goods-tile__price-value").text
                with open("products.txt", "a", encoding="UTF-8") as file:
                    file.write(f"{title_}  {price}\n")
                print(title_, price)
            except:
                title_ = products[j].find("span", class_="goods-tile__title").text
                print(f"{title_} - знижки немає")
