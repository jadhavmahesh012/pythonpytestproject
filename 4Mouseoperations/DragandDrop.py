import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj=Service("C:\\Mahesh\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

act=ActionChains(driver)

rome_ele=driver.find_element(By.ID,"box6")
italy_ele=driver.find_element(By.ID,"box106")
act.drag_and_drop(rome_ele,italy_ele).perform()  # drag and drop opration
time.sleep(5)

wsh_ele=driver.find_element(By.ID,"box3")
italy_ele=driver.find_element(By.ID,"box103")
act.drag_and_drop(wsh_ele,italy_ele).perform()  # drag and drop opration
time.sleep(5)

Oslo_ele=driver.find_element(By.ID,"box1")
norway_ele=driver.find_element(By.ID,"box101")
act.drag_and_drop(Oslo_ele,norway_ele).perform()  # drag and drop opration
time.sleep(5)

madrid_ele=driver.find_element(By.ID,"box7")
spain_ele=driver.find_element(By.ID,"box107")
act.drag_and_drop(madrid_ele,spain_ele).perform()
time.sleep(5)

copen_ele=driver.find_element(By.ID,"box4")
denmark_ele=driver.find_element(By.ID,"box104")
act.drag_and_drop(copen_ele,denmark_ele).perform()
time.sleep(5)

