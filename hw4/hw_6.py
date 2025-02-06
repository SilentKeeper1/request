import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    top_books = [book.find("h3").find("a")["title"]
                 for book in books
                 if book.find("p", class_="star-rating")
                 and "Five" in book.find("p", class_="star-rating").get("class", [])]
    with open("../top_books.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(top_books))
    print("Список книг з рейтингом 5 stars збережено у 'top_books.txt'")
else:
    print("Помилка отримання даних від сайту")