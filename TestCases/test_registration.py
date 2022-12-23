from Base import initialiseDriver
from Base.configReader2 import readLocator
from Pages import registrationPage


def test_verifyRegistrationPageIsWorkingFine():
    driver = initialiseDriver.start()
    print(readLocator("Registration", "firstName"))
    r = registrationPage.registration(driver)
    r.enterDataByName(readLocator("Registration", "firstName"), "user123")
