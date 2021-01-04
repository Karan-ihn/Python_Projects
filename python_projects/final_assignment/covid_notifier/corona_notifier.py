from plyer import notification
import requests
from bs4 import BeautifulSoup
import html5lib
import time

def covid_notify(title,total_cases,recovered,casualities):
    title = title
    message = 'Total cases : '+total_cases+'\nRecovered : '+recovered+'\nCasualities : '+casualities
    notification.notify(
        title = title,
        message = message,
        timeout = 10,
        app_icon = 'covid.ico'
    )
    


url = requests.get('https://www.worldometers.info/coronavirus/country/india/')
soup = BeautifulSoup(url.content,'html5lib')
soup.prettify()

stats = soup.find_all('div',class_='maincounter-number')
total_cases = stats[0].span.text
recovered = stats[2].span.text
casualities = stats[1].span.text


covid_notify('Covid Status : India',total_cases,recovered,casualities)
