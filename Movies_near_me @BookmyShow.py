import requests
from bs4 import BeautifulSoup


def movies_in_theatre(url):
    code=requests.get(url)
    text=code.text
    soup=BeautifulSoup(text,"html.parser")
    movie_name="Movies_near_me @BookmyShow"+"\n\n"
    i=1
    for link in soup.findAll('a',{'class':'__movie-name'}):
        title=link.get('title')
        link="https://in.bookmyshow.com"+link.get('href')
        movie_name+=str(i)+"."+title+" "+link+"\n"
        i+=1

    fw = open('Movies_near_me.txt', 'w')
    fw.write(movie_name)
    fw.close()

city=input("Enter a valid city name: ")
movies_in_theatre("https://in.bookmyshow.com/"+city+"/movies")