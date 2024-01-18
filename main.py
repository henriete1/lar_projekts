import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from datetime import date, timedelta,datetime

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

date_str = ""

if date_str == "":
    today=date.today()

else:
    today = datetime.strptime(date_str, '%Y-%m-%d').date()

yesterday= today - timedelta(days=1)

print(today, yesterday)

month1=yesterday.strftime('%B')
year1=yesterday.strftime('%Y')

month=today.strftime('%B')
year=today.strftime('%Y')


if month1==month and year1==year:
    url = "https://www.accuweather.com/en/lv/riga/225780/"+(month.lower())+"-weather/225780?year="+year
    url1=url

elif year1==year:
    url = "https://www.accuweather.com/en/lv/riga/225780/"+(month.lower())+"-weather/225780?year="+year
    url1 = "https://www.accuweather.com/en/lv/riga/225780/"+(month1.lower())+"-weather/225780?year="+year

else:
    url = "https://www.accuweather.com/en/lv/riga/225780/"+(month.lower())+"-weather/225780?year="+year
    url1 = "https://www.accuweather.com/en/lv/riga/225780/"+(month1.lower())+"-weather/225780?year="+year1



driver.get(url)
time.sleep(2)
driver.get(url1)

driver.find_element(By.XPATH, "//html/body/div[2]/div[2]/div[1]/div[2]/div[2]/button[1]").click()

time.sleep(2)





time.sleep(3)

"""
url = "https://www.accuweather.com/en/lv/riga/225780/weather-forecast/225780?city=riga"
driver.get(url)
time.sleep(2)

driver.find_element(By.XPATH, "//html/body/div[2]/div[2]/div[1]/div[2]/div[2]/button[1]").click()

time.sleep(2)

find1 = driver.find_element(By.CLASS_NAME, "temp")
temperature=(find1.get_attribute("outerHTML"))

degree=(temperature.find("°")+1)
temperature=(temperature[18:degree]+"C")

print(temperature)

print("sssss")

"""
driver.quit()