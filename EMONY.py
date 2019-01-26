import requests
from bs4 import BeautifulSoup


def movies_in_theatre(url, city):
    code = requests.get(url)
    text = code.text
    soup = BeautifulSoup(text, "html.parser")
    movie_name = "Movies_near_me @BookmyShow" + "\n" + "Your City -> " + city + "\n\n"

    i = 1
    for link in soup.findAll('div', {'class': 'card-container wow fadeIn movie-card-container'}):
        title = link.find('a')['title']
        link = "https://in.bookmyshow.com" + link.find('a')['href']
        movie_name += str(i) + "." + title + " -> " + link + "\n"
        i += 1

    fw = open('Movies_near_me.txt', 'w')
    fw.write(movie_name)
    fw.close()


city = input("Enter a valid city name: ")
movies_in_theatre("https://in.bookmyshow.com/" + city + "/movies", city)
