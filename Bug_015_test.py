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
    # Klik tab Knowledge Center
    element = WebDriverWait(driver, 5).until( 
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/ul/li[6]/a'))
    ) 
    element.click()
    time.sleep(3) 

    # Ubah ke mode bahasa indonesia
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/ul/li[9]/div/a[1]'))
    )
    # Klik elemen menggunakan JS (Karena tidak bisa diklik hanya dengan selenium)
    driver.execute_script("arguments[0].click();", element)

    # Scroll ke button Let's Learn
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/section[2]/div/div[1]/div[3]/a'))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", element)  
    time.sleep(3)