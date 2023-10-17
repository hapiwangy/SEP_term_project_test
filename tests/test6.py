from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import sys
# testcase6 

def test6(randomgroupname:str, randomaccount:str, randompassword:str):
    # open browser
    driver = webdriver.Chrome()
    driver.get(r"http://127.0.0.1:5000")
    time.sleep(2)

    # fill in wrong account and password
    group = Select(driver.find_element(By.NAME, 'groupname'))
    account = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    group.select_by_visible_text(randomgroupname)
    time.sleep(1)
    account.send_keys(randomaccount)
    time.sleep(1)
    password.send_keys(randompassword)
    time.sleep(2)

    # press login button
    login = driver.find_element(By.NAME, "loginbutton")
    login.click()
    time.sleep(3)

    # 處理結束狀態
    try:
        message = driver.find_element(By.ID, "showFail")
    except Exception:
        return 1

    driver.close()
    return 0

if __name__ == "__main__":
    print(main())