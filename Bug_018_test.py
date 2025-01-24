import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver import ChromeOptions

@pytest.fixture()

def driver():
    driver = webdriver.Chrome()
    driver.get('https://javan.co.id/')
    driver.maximize_window()
    yield driver
    driver.quit()

def test(driver): 
    # Klik tab Career
    element = WebDriverWait(driver, 5).until( 
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/ul/li[7]/a'))
    ) 
    element.click()
    time.sleep(3) 

    # Klik job Helpdesk
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/form/section[2]/div[2]/div[1]/div/div/a[2]'))
    )
    element.click()
    time.sleep(3) 

    # Scroll ke content
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/section/div/div[1]/div[2]/ol[2]'))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", element)  
    time.sleep(3)
