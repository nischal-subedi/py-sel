import os
from dotenv import load_dotenv
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
#from selenium.webdriver.firefox.service import Service

load_dotenv()

# Act on Deprecation Notice for firefox binary
#option = webdriver.FirefoxOptions()
#option.binary_location = "/Applications/Firefox Developer Edition.app/Contents/MacOS/firefox-bin"
#driverService = Service("/opt/homebrew/bin/geckodriver")
#driver = webdriver.Firefox(service=driverService, options=option)


# set the path to the Firefox binary
binary = FirefoxBinary('/Applications/Firefox Developer Edition.app/Contents/MacOS/firefox-bin')
# initialize the Firefox webdriver
driver = webdriver.Firefox(firefox_binary=binary)

# navigate to the website
#driver.get("https://webservices.ignou.ac.in/Pre-Question/")
driver.get(os.getenv('BASE_URL'))

# Follow links using XPATH
link1 = driver.find_element(By.XPATH, "/html/body/table[1]/tbody/tr[4]/td/table/tbody/tr[6]/td[1]/b/strong/a")
link1.click()

time.sleep(1)

link2 = driver.find_element(By.XPATH, "/html/body/div/table/tbody/tr[109]/td[3]/p/b/a")
link2.click()

time.sleep(3)

link3 = driver.find_element(By.XPATH, "/html/body/div/table/tbody/tr[11]/td[4]/p/span/a")
link3.click()

#print("This is the link", link3)
#downloadPDF = driver.get(link3)

# close the webdriver
driver.quit()


time.sleep(4)
# close the webdriver

#Fix driver connection issues when closing

driver.close()

