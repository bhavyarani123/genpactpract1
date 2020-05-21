from selenium import webdriver
import pytest
import allure
from pages.homePage import HomePage
from pages.loginPage import loginPage
from utils import utils as utils
import moment


@pytest.mark.usefixtures("test_setup")
class Testlogin():

    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)
        login = loginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)


    def test_logout(self):
        try:
            driver = self.driver
            homepage = HomePage(driver)
            homepage.click_welcome()
            homepage.click_logout()
            x= driver.title
            assert x == "abc"

        except AssertionError as error:
            print("Assertion error occured")
            print(error)
            currTime = moment.now().strftime("%H-%M-%S_%d-%m-%Y")
            testName = utils.whoiami()
            screenshotName = testName+currTime
            allure.attach(self.driver.get_screenshot_as_png(),name=screenshotName,attachment_type=allure.attachment_type.png)
            driver.get_screenshot_as_file("C:/Users/bhavy/PycharmProjects/genpactpract/screenshots"+screenshotName+".png")
            raise

        except:
            print("There was an exception")
            currTime = moment.now().strftime("%H-%M-%S_%d-%m-%Y")
            testName = utils.whoiami()
            screenshotName = testName + currTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,attachment_type=allure.attachment_type.png)

            raise

        else:
            print("No exception occured")

        finally:
             print("I am inside finally block")

