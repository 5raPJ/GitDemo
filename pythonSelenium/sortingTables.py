from selenium import webdriver
from selenium.webdriver.common.by import By

browserSortedVegies = []
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

#click on column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

#collect all veggie names --> BrowserSortedveggieList (B A, C)
veggieElements = driver.find_elements(By.XPATH, "//tr/td[1]")
for vegi in veggieElements:
    browserSortedVegies.append(vegi.text)

originalSortedBrowserList = browserSortedVegies.copy()
#sort this BrowserSortedveggieList --> newSortedList  -->(A,B,C)
browserSortedVegies.sort()
assert browserSortedVegies == originalSortedBrowserList
