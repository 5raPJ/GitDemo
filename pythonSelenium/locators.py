from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")

#id, xpath, cssselector, classname, name. linktext
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

# Xpath//tagName[@attribute='value'] --> //input[@type='submit']
#css  tagname[atttribute='value'], #id
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Petra Janc")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

#static dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(1)
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
#dropdown.select_by_value()

driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("HalloAgin")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
time.sleep(3)
