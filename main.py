import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
data = response.text

Soup = BeautifulSoup(data, "html.parser")
All_Movies = Soup.find(name="h3", class_="title")
Movies_list =[movie.getText() for movie in All_Movies]
Movies = Movies_list[::-1]
print(Movies)

with open("Movies_list.txt", mode="w") as file:
    for movie in Movies:
        file.write(f"{movie}\n")
