# Author - R.Murali
# Created Date - 11th April 2022
import time

from selenium import webdriver

# This method is used to launch the chrome browser
def launchBrowser():

    global driver

    # 1. Calling the chrome method to launch the chrome browser
    # 2. Need to pass the chrome driver path as the argument to the Chrome method
    # 3. Need to store the Launched chrome driver as driver variable to use the launched driver in future steps
    # 4. We can use the driver from it's project itself. So  that we need to use (..\) in driver path.
    driver = webdriver.Chrome(executable_path="..\chromedriver.exe")



def maximizeWindow():

    # We can maximize the driver in 2 ways
    # 1. fullscreen_window()
    # 2. maximize_window()
    # line(26-28)
    driver.fullscreen_window()

    driver.maximize_window()


def get(url):
    # The get() is used to hit the link
    # We need to pass an argument to the get method as the String value
    # It will not return any value
    driver.get(url)



def basic():
    launchBrowser()
    maximizeWindow()
    get("https://www.google.com/")


# Calling the basic method, Because method only runs when it is called.
basic()