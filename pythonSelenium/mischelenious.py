from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")

chrome_options.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(chrome_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

driver.get_screenshot_as_file("screen.png")
time.sleep(3)