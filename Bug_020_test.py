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
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/ul/li[7]/a'))
    ) 
    element.click()
    time.sleep(3) 

    # Klik job QA Magang
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/form/section[2]/div[2]/div[2]/div/div/a[2]'))
    )
    element.click()
    time.sleep(3)  

    # Klik Apply job
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/section/div/div[2]/div[1]/div[3]/a[1]'))
    )
    element.click()
    time.sleep(5) 

    # Full Name
    input_element = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[2]/div[2]/form/div/div/div[1]/div[1]/div/input')
    input_element.send_keys("Test QA")
    time.sleep(2) 

    # Email Address
    input_element = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[2]/div[2]/form/div/div/div[1]/div[2]/div/input')
    input_element.send_keys("TestQA@gmail.com")
    time.sleep(3) 

    # Phone
    input_element = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[2]/div[2]/form/div/div/div[1]/div[3]/div/input')
    input_element.send_keys("Test QA")
    time.sleep(2) 

    # Gender  
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[2]/div[2]/form/div/div/div[1]/div[7]/select'))
    )
    element.click()
    time.sleep(2) 
    
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[2]/div[2]/form/div/div/div[1]/div[7]/select/option[2]'))
    )
    element.click()
    time.sleep(3) 

    # Education  
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[2]/div[2]/form/div/div/div[1]/div[8]/select'))
    )
    element.click()
    time.sleep(2) 
    
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[2]/div[2]/form/div/div/div[1]/div[8]/select/option[4]'))
    )
    element.click()
    time.sleep(3) 

    # name education
    input_element = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[2]/div[2]/form/div/div/div[1]/div[9]/div/input')
    input_element.send_keys("Test QA")
    time.sleep(2) 

    # Join Date
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[2]/div[2]/form/div/div/div[1]/div[10]/select'))
    )
    element.click()
    time.sleep(2) 
    
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[2]/div[2]/form/div/div/div[1]/div[10]/select/option[2]'))
    )
    element.click()
    time.sleep(3)
    
    # Which one do you prefer?
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[2]/div[2]/form/div/div/div[1]/div[11]/select'))
    )
    element.click()
    time.sleep(2) 
    
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[2]/div[2]/form/div/div/div[1]/div[11]/select/option[2]'))
    )
    element.click()
    time.sleep(3) 

    # Current Address
    input_element = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[2]/div[2]/form/div/div/div[2]/div[1]/div/textarea')
    input_element.send_keys("Test QA Test QA Test QA Test QA Test QA Test QA Test QA Test QA Test QA Test QA ")
    time.sleep(2) 

    # About
    input_element = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[2]/div[2]/form/div/div/div[2]/div[2]/div/textarea')
    input_element.send_keys("Test QA Test QA Test QA Test QA Test QA Test QA Test QA Test QA Test QA Test QA ")
    time.sleep(2) 

    # How do you know this opportunity?
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[2]/div[2]/form/div/div/div[2]/div[5]/select'))
    )
    element.click()
    time.sleep(3) 
    
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[2]/div[2]/form/div/div/div[2]/div[5]/select/option[8]'))
    )
    element.click()
    time.sleep(3) 

    # Are you a smoker?
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[2]/div[2]/form/div/div/div[2]/div[6]/select'))
    )
    element.click()
    time.sleep(3) 
    
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[2]/div[2]/form/div/div/div[2]/div[6]/select/option[2]'))
    )
    element.click()
    time.sleep(3) 

    # Are you a difabled ?
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[2]/div[2]/form/div/div/div[2]/div[7]/select'))
    )
    element.click()
    time.sleep(3) 
    
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[2]/div[2]/form/div/div/div[2]/div[7]/select/option[2]'))
    )
    element.click()
    time.sleep(3) 

    # Typing per WPM
    input_element = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[2]/div[2]/form/div/div/div[2]/div[8]/div/input')
    input_element.send_keys("52")
    time.sleep(5) 

    # Upload CV
    file_input = WebDriverWait(driver, 10).until( 
        # EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
        EC.presence_of_element_located((By.XPATH, '//*[@id="in_resume_cv"]'))
    )
    driver.execute_script("arguments[0].scrollIntoView();", file_input)

    # Kirim file
    file_path = r'C:\Users\ASUS\Pictures\A.pdf'
    file_input.send_keys(file_path)
    time.sleep(5) 

    # Upload Image
    file_input = WebDriverWait(driver, 10).until(  
        EC.presence_of_element_located((By.XPATH,'//*[@id="in_typing_test_result"]'))
        # EC.presence_of_element_located((By.XPATH, '//*[@id="in_resume_cv"]'))
    )
    driver.execute_script("arguments[0].scrollIntoView();", file_input)

    # Kirim file
    file_path = r'C:\Users\ASUS\Pictures\kwm.PNG'
    file_input.send_keys(file_path)
    time.sleep(3)  # Tunggu proses selesai

    # Klik Apply job
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[2]/div[2]/form/div/div/div[3]/button'))
    )
    element.click()
    time.sleep(10) 

    

    