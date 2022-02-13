from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.rightmove.co.uk/")
driver.find_element(By.XPATH,'//*[@id="_3OuiRnbltQyS534SB4ivLV"]/div/div/div/div/input').send_keys("Stockwood,Bristol")
driver.find_element(By.XPATH,'//*[@id="_3OuiRnbltQyS534SB4ivLV"]/div/div/div/button[1]').click()

propertytype = Select(driver.find_element(By.XPATH,'//*[@id="displayPropertyType"]'))
propertytype.select_by_index(1)
radius = Select(driver.find_element(By.XPATH,'//*[@id="radius"]'))
radius.select_by_index(7)
MaxPrice = Select(driver.find_element(By.XPATH,'//*[@id="maxPrice"]'))
MaxPrice.select_by_value('350000')
Rooms = Select(driver.find_element(By.XPATH,'//*[@id="minBedrooms"]'))
Rooms.select_by_value('3')
driver.find_element(By.XPATH,'//*[@id="submit"]').click()
input('Test GIT')