from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def test10(randomgroupname: str, randomaccount: str, randompassword: str, thing: dict):
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
    # Count cards before deleting post
    rows = driver.find_element(By.CLASS_NAME, 'table').find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
    countRows = len(rows)

    # Fill date
    date = driver.find_element(By.NAME, 'date')
    date.send_keys(thing['date'])

    # Fill thing
    date = driver.find_element(By.NAME, 'thing')
    date.send_keys(thing['thing'])

    # Fill expense
    date = driver.find_element(By.NAME, 'expense')
    date.send_keys(thing['expense'])
    time.sleep(1)

    #Click addthing button
    addThing = driver.find_element(By.NAME, 'addthing')
    addThing.click()
    time.sleep(1)

    try:
        countCurrentRows = len(driver.find_element(By.CLASS_NAME, 'table').find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr'))
        assert countCurrentRows == countRows + 1
    except Exception:
        return 1
    
    driver.close()
    return 0

