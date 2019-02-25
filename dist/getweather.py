from bs4 import BeautifulSoup
from selenium import webdriver
import re
from function import speak


def weatherinfo(location,location_table):
    driver = webdriver.Firefox(executable_path='geckodriver.exe')
    url=list(location_table.keys())[list(location_table.values()).index(location)]
    driver.get('https://www.cwb.gov.tw'+url)
    res = BeautifulSoup(driver.page_source, "lxml")
    weather_info= res.select('#ftext')[0].text
    weather_info = re.sub(r'http\S+', '', weather_info)
    weather_info = re.sub(r'..:\S+', '', weather_info)
    speak("今日%s天氣狀況" %(location) )
    speak(weather_info)

def all_location():
    location=[]
    location_url=[]
    with open('location.csv') as fp:
        for locations in fp.readlines():
            locations=re.sub(r'\n', '', locations)
            locations = locations.split(',')
            location_url.append(locations[0])
            location.append(locations[1])
    location_table=dict(zip(location_url,location))
    return  location_table
