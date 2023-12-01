import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
# Write your code below this line 👇

response = requests.get(URL)
empireonline_page = response.text
soup = BeautifulSoup(empireonline_page, "html.parser")

films = [article.getText() for article
         in soup.find_all(name="h3", class_="title")[::-1]]

#print(films)

with open("films.txt", mode="w") as file:
    for film in films:
        file.write(f"{film}\n")
