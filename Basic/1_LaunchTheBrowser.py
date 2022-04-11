# Author - R.Murali
# Created Date - 11th April 2022
import time

from selenium import webdriver

# This method is used to launch the chrome browser
def launchBrowser():

    # 1. Calling the chrome method to launch the chrome browser
    # 2. Need to pass the chrome driver path as the argument to the Chrome method
    # 3. Need to store the Launched chrome driver as driver variable to use the launched driver in future steps
    # 4. We can use the driver from it's project itself. So  that we need to use (..\) in driver path.
    driver = webdriver.Chrome(executable_path="..\chromedriver.exe")


# Calling the Launch Browser method, Because method only runs when it is called.
launchBrowser()
