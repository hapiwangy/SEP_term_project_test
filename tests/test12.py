# testcase 12

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def test12(randomgroupname: str, randomaccount: str, randompassword: str):
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

    # Click showfullpost button
    showFullPost = driver.find_elements(By.NAME, 'showfullpost')[-1]
    showFullPost.click()
    time.sleep(1)

    # Test
    # Count comments before deleting post
    comments = driver.find_elements(By.CLASS_NAME, 'card')
    countComments = len(comments)

    # Delete comment
    deleteComment = driver.find_elements(By.NAME, 'deletecomment')[-1]
    print(deleteComment)
    deleteComment.click()
    time.sleep(1)

    try:
        countCurrentComments = len(driver.find_elements(By.CLASS_NAME, 'card'))
        assert countCurrentComments == countComments - 1
    except Exception:
        return 1
    
    driver.close()
    return 0

