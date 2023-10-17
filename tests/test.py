from selenium import webdriver
from selenium.webdriver.common.by import By

import time


# testcase 1


def test(randomgroupname:str, randomaccount:str, randompassword:str) -> int:
    # open browser
    driver = webdriver.Chrome()
    driver.get(r"http://127.0.0.1:5000/admin")
    time.sleep(2)

    # 填入帳號密碼
    account, password = driver.find_element(By.ID, "username"), driver.find_element(By.ID, "password")
    groupname = driver.find_element(By.ID, "groupname")
    account.send_keys(randomaccount)
    password.send_keys(randompassword)
    groupname.send_keys(randomgroupname)

    # 執行註冊動作
    register = driver.find_element(By.NAME, "establishbutton")
    register.click()
    time.sleep(2)

    # 處理結束狀態
    try:
        message = driver.find_element(By.ID, "showSuccessful")
    except Exception:
        return 1

    driver.close()
    return 0


