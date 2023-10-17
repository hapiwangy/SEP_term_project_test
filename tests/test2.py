from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


# testcase 2


def test2(randomgroupname:str, randomaccount:str, randompassword:str) -> int:
    # open browser
    driver = webdriver.Chrome()
    driver.get(r"http://127.0.0.1:5000/signup")
    time.sleep(2)

    # 填入帳號密碼
    account, password = driver.find_element(By.ID, "username"), driver.find_element(By.ID, "password")
    group = Select(driver.find_element(By.NAME, 'groupname'))
    group.select_by_visible_text(randomgroupname)
    account.send_keys(randomaccount)
    password.send_keys(randompassword)

    # 執行註冊動作
    register = driver.find_element(By.NAME, "establish")
    register.click()
    time.sleep(2)

    # 處理結束狀態
    try:
        driver.find_element(By.ID, "showSuccessful")
    except Exception:
        return 1

    driver.close()
    return 0
