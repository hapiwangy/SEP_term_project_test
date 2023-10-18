# testcase 11

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def test11(randomgroupname: str, randomaccount: str, randompassword: str):
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

    # Click login button(login as admin)
    loginButton = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/form/button[1]')
    loginButton.click()
    time.sleep(2)

    # Test
    # Count cards before deleting post
    cards = driver.find_elements(By.CLASS_NAME, 'card')
    countCards = len(cards)

    # Delete post button
    deletepost = driver.find_elements(By.NAME, 'deletepost')[-1]
    deletepost.click()
    time.sleep(10)

    try:
        countCurrentCards = len(driver.find_elements(By.CLASS_NAME, 'card'))
        assert countCurrentCards == countCards - 1
    except Exception:
        return 1
    
    driver.close()
    return 0
