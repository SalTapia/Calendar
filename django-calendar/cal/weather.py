import requests
from bs4 import BeautifulSoup  
from urllib.request import urlopen

site = "https://forecast.weather.gov/MapClick.php?lat=39.732&lon=-121.842"
html = urlopen(site)
soup = BeautifulSoup(html,"lxml")
week = soup.find("div",id="seven-day-forecast-body")
items = soup.find_all("div",class_ = "tombstone-container")

day=[]; descreption = []; temp = []
for item in items:
    day.append(item.find(class_="period-name").get_text(" "))
    descreption.append(item.find(class_="short-desc").get_text(" "))
    temp.append(item.find(class_="temp").get_text(" "))
