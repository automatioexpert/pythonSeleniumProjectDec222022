from selenium import webdriver
from selenium.webdriver.common.by import By

class registration:

    def __init__(self, driverObj):
        global driver
        driver = driverObj

    def enterDataByName(self, locator, data):
        driver.find_element(By.NAME, locator).send_keys(data)




