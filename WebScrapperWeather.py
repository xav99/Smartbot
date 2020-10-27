import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from regex_search import searchExclude

def returnWeather(url="https://weather.theage.com.au/local-forecast/vic/melbourne"):
    '''
    Retrieves the weather from our specified url
    '''
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    weather = soup.find('div', attrs={'class':'ff_current_temp'}) 
    weather = str(weather)
    weather = searchExclude('a-z=_"<> / \n °', weather) # strips all unnessacary characters so we can just get the numbers
    x=""
    for i in weather: # puts the string back together 
        x+= i
    weather = x
    return weather

