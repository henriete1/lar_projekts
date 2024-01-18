import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from datetime import date, timedelta,datetime
from calendar import monthrange

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)


sar=[]
date_str = "2024-01-01"



if date_str == "":
    today=date.today()

else:
    today = datetime.strptime(date_str, '%Y-%m-%d').date()

yesterday= today - timedelta(days=1)

print(today, yesterday)

month1=yesterday.strftime('%B')
month_days1=monthrange((int(yesterday.strftime('%Y'))), (int(yesterday.strftime('%m'))))
year1=yesterday.strftime('%Y')

month=today.strftime('%B')
month_days=monthrange((int(today.strftime('%Y'))), (int(today.strftime('%m'))))
year=today.strftime('%Y')


print(today.strftime('%Y'))
print(today.strftime('%m'))

print(monthrange((int(today.strftime('%Y'))), (int(today.strftime('%m')))))

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

#datetoday="7"
#print(datetoday)

driver.find_element(By.XPATH, "//html/body/div[2]/div[2]/div[1]/div[2]/div[2]/button[1]").click()

for i in range (1, 36):

    find = driver.find_element(By.XPATH, "/html/body/div/div[7]/div[1]/div[1]/div[2]/div/div[2]/a["+str(i)+"]/div[1]/div")
    day = (find.get_attribute("outerHTML"))
    day = R"{}".format(day)
    #print(day)
    if str(int(today.strftime('%d'))) in day:
        find1=driver.find_element(By.XPATH, "/html/body/div/div[7]/div[1]/div[1]/div[2]/div/div[2]/a["+str(i)+"]/div[2]")
        #find1= driver.find_element(By.CLASS_NAME, "temp")
        temp= (find1.get_attribute("outerHTML"))

        #day.find
        high=(temp.find("high")+15)
        degree=(temp.find("°")+1)
        
        temperature=(temp[high:degree]+"C")
        #sar.append(day)
        #sar.append(temp)
        sar.append(temperature)
    #sar.append("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    #find.clear()



print(sar)
print(len(sar))

if int(today.strftime('%d')) < 6:
    print(sar[0])
if int(today.strftime('%d')) > 26:
    print(sar[1]) 
#print(sar[2])

driver.get(url1)



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