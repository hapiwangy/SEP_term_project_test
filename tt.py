from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def main():
    # Get webdriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://127.0.0.1:5000")
    time.sleep(1)

    # Preparing for test
    # Select group
    groupname = Select(driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/form/div[1]/select'))
    groupname.select_by_visible_text(u"happy")

    # Enter username
    username = driver.find_element(By.XPATH, '//*[@id="username"]')
    username.send_keys("kevin123")

    # Enter password
    password = driver.find_element(By.XPATH, '//*[@id="password"]')
    password.send_keys("kevin123")
    time.sleep(1)

    # Click login button
    loginButton = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/form/button[1]')
    loginButton.click()
    time.sleep(2)

    # Click showfullpost button
    showFullPost = driver.find_elements(By.NAME, 'showfullpost')[-1]
    showFullPost.click()
    time.sleep(1)

    # Test
    # Count comments before adding comment
    comments = driver.find_elements(By.CLASS_NAME, 'card')
    countComments = len(comments)

    # Add comment
    newComment = driver.find_element(By.XPATH, '//*[@id="new-comment"]')
    newComment.send_keys("test comment")
    time.sleep(1)

    # Click addnewcomment button
    addNewComment = driver.find_element(By.NAME, 'addnewcomment')
    addNewComment.click()
    time.sleep(1)

    try:
        countCurrentComments = len(driver.find_elements(By.CLASS_NAME, 'card'))
        assert countCurrentComments == countComments + 1
    except Exception:
        return 1
    
    driver.close()
    return 0

if __name__ == "__main__":
    print(main())