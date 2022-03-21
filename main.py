from bs4 import BeautifulSoup
import re
import requests


def main(emotion):
    if emotion == "Sad":
        url = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc'
    elif emotion == "Disgust":
        url = 'http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter, asc'
    elif emotion == "Anger":
        url = 'http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc'
    elif emotion == "Anticipation":
        url = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
    elif emotion == "Fear":
        url = 'http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc'
    elif emotion == "Enjoyment":
        url = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
    elif emotion == "Trust":
        url = 'http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc'
    elif emotion == "Surprise":
        url = 'http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter, asc'

    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, 'lxml')
    title = soup.find_all("a", attrs={"href": re.compile(r'\/title\/tt+\d*\/')})
    return title


if __name__ == '__main__':
    emotion = input("Enter Emotion >")
    a = main(emotion)
    count = 0
    if emotion == "disgust" or emotion == "anger" or emotion == "surprise":
        for i in a:
            tmp = str(i).split('>;')
            if len(tmp) == 3:
                print(tmp[1][:-3])
            if count > 13:
                break
            count += 1
    else:
        for i in a:
            tmp = str(i).split('>')
            if len(tmp) == 3:
                print(tmp[1][:-3])
            if count > 11:
                break
            count +=1
