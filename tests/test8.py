from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def test8(randomgroupname: str, randomaccount: str, randompassword: str, postcontent: str):
    # Get webdriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://127.0.0.1:5000")
    time.sleep(1)

    # Preparing for test
    # Select group
    groupname = Select(driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/form/div[1]/select'))
    groupname.select_by_visible_text(randomgroupname)

    # Enter username
    username = driver.find_element(By.XPATH, '//*[@id="username"]')
    username.send_keys(randomaccount)

    # Enter password
    password = driver.find_element(By.XPATH, '//*[@id="password"]')
    password.send_keys(randompassword)
    time.sleep(1)

    # Click login button
    loginButton = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/form/button[1]')
    loginButton.click()
    time.sleep(2)

    # Test
    # Card number before submitting post
    card = driver.find_elements(By.CLASS_NAME, 'card')
    cardNumber = len(card)

    # Post content
    postContent = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/form/div/div[1]/textarea')
    postContent.send_keys(postcontent)
    time.sleep(1)

    # Posting button
    postButton = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/form/div/div[2]/button')
    postButton.click()
    time.sleep(1)

    # Post content
    postContent = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/form/div/div[1]/textarea')
    postContent.send_keys(postcontent+"omg so cool!")
    time.sleep(1)

    # Posting button
    postButton = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/form/div/div[2]/button')
    postButton.click()
    time.sleep(1)
    try:
        assert len(driver.find_elements(By.CLASS_NAME, 'card')) == cardNumber + 2
    except Exception:
        return 1
    
    driver.close()
    return 0
