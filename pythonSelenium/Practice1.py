from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.implicitly_wait(14)
driver.maximize_window()
#click on blinking test
driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()

openwindows = driver.window_handles
driver.switch_to.window(openwindows[1])
#search for email
email = driver.find_element(By.CSS_SELECTOR, "a[href='mailto:mentor@rahulshettyacademy.com']").text
print(email)

#enter email to login page
driver.switch_to.window(openwindows[0])
driver.find_element(By.CSS_SELECTOR, "#username").send_keys(email)
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("343444")
driver.find_element(By.CSS_SELECTOR, "#terms").click()
driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
#check error message
errorText = driver.find_element(By.CSS_SELECTOR, ".alert-danger").text
print(errorText)
assert "Incorrect username/password." == errorText
