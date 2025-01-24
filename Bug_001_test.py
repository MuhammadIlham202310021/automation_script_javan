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
    # Klik tab Company Information
    element = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/ul/li[2]/div'))
    ) 
    element.click()
    time.sleep(3)

    # klik tab management team
    element = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/ul/li[2]/div/ul/li[2]/a'))
    )
    element.click()
    time.sleep(3)

    # Ubah ke mode bahasa indonesia
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/ul/li[9]/div/a[1]'))
    )
    # Klik elemen menggunakan JS (Karena tidak bisa diklik hanya dengan selenium)
    driver.execute_script("arguments[0].click();", element)

    # Scroll tapi jangan diklik
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="seeMore"]'))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", element) 
    time.sleep(10)
