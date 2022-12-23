
from selenium import webdriver

driver = webdriver.Chrome()

def start():

    driver.get("https://www.way2automation.com/way2auto_jquery/registration.php#load_box")
    driver.maximize_window()

start()

def stop():
    driver.close()
