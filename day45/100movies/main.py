import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
stuff = response.text

soup = BeautifulSoup(stuff, 'html.parser')

title_tags = soup.find_all(name='h3', class_='title')
titles = [title.getText() for title in title_tags][::-1]

with open('movies.txt', mode='w') as f:
    for title in titles:
        f.write(f"{title}\n")


