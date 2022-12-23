from  selenium import  webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com")
print(driver.title)
driver.find_element(By.ID,"").click()
driver.close()
