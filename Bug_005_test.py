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
    # Klik tab portfolio
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/ul/li[5]/div'))
    ) 
    element.click()
    time.sleep(3)

    # klik tab portfolio
    element = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/ul/li[5]/div/ul/li[1]/a'))
    )
    element.click()
    time.sleep(3)
    
    # Klik content
    element = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/section[2]/div/div[1]/div[2]/a'))
    )
    element.click()
    time.sleep(3)

