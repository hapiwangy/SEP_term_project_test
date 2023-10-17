from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import sys
# testcase7 

def test7(randomgroupname:str, randomaccount:str, randompassword:str):
    # open browser
    driver = webdriver.Chrome()
    driver.get(r"http://127.0.0.1:5000")
    time.sleep(2)

    # fill in account and password
    group = Select(driver.find_element(By.NAME, 'groupname'))
    account = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    group.select_by_visible_text(randomgroupname)
    account.send_keys(randomaccount)
    password.send_keys(randompassword)

    # press login button
    login = driver.find_element(By.NAME, "loginbutton")
    login.click()
    time.sleep(2)

    # press logout button
    logout = driver.find_element(By.NAME, "logout")
    logout.click()
    time.sleep(3)

    # 處理結束狀態
    try:
        message = driver.find_element(By.NAME, "loginbutton")
    except Exception:
        return 1

    driver.close()
    return 0

