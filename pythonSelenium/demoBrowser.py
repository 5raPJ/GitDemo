import time

from selenium import webdriver
#from selenium.webdriver.chrome.service import Service

#service_obj = Service("C:\Users\jancp\Downloads\chromedriver-win64/chromedriver.exe")
#driver = webdriver.chrome(service=service_obj)

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

time.sleep(2)