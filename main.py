from bs4 import BeautifulSoup
import requests
import pandas as pd

print("Enter Emotion >")
print("1.Sad")
print("2.Disgust")
print("3.Anticipation")
print("4.Fear")
print("5.Enjoyment")
print("6.Trust")
print("7.Surprise")
emotion = input("Enter Choice: ")

if emotion == "sad" or "Sad":
    url = "https://www.imdb.com/search/title/?genres=drama&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL, asc"

elif emotion == "disgust" or "Disgust":
    url = "https://www.imdb.com/search/title/?genres=horror&explore=title_type, asc"

elif emotion == "anger" or "Anger":
    url = "https://www.imdb.com/search/title/?genres=action&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL, asc"

elif emotion == "anticipation" or "Anticipation":
    url = "https://www.imdb.com/search/title/?genres=thriller&title_type=feature&explore=genres&pf_rd_m, asc"

elif emotion == "fear" or "Fear":
    url = "https://www.imdb.com/search/title/?genres=horror&explore=title_type, asc"

elif emotion == "enjoyment" or "Enjoyment":
    url = "https://www.imdb.com/search/title/?genres=adventure&title_type=feature&explore=genres&pf_rd_m, asc"

elif emotion == "trust" or "Trust":
    url = "https://www.imdb.com/search/title/?genres=romance&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL, asc"

elif emotion == "surprise" or "Surprise":
    url = "https://www.imdb.com/search/title/?genres=fantasy&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL, asc"

response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, 'lxml')

movie_name = []
year = []
time = []
rating = []

movie_data = soup.find_all('div', attrs={'class': 'lister-item mode-advanced'})
for store in movie_data:
    name = store.h3.a.text
    movie_name.append(name)

    year_of_release = store.h3.find('span', class_='lister-item-year text-muted unbold').text.replace('(', '').replace(')', '').replace(' ', '')
    year.append(year_of_release)

    runtime = store.p.find('span', class_='runtime').text.replace(' min', '') if store.find('span', class_='runtime') else 'N/A'
    time.append(runtime)

    rate = store.find('div', class_='inline-block ratings-imdb-rating').text.replace('\n', '') if store.find('div', class_='inline-block ratings-imdb-rating') else 'N/A'
    rating.append(rate)

movie_df = pd.DataFrame({'Name: ': movie_name, 'Year of release': year, 'Watch-time: ': time, 'Rating: ': rating})
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
movie_df.index += 1
print(movie_df)
