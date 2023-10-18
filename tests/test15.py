from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def test15(randomgroupname: str, randomaccount: str, randompassword: str):
  driver = webdriver.Chrome()
  driver.get(r"http://127.0.0.1:5000")
  time.sleep(1)

  # fill in account and password
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
  time.sleep(2)

  try:
    message = driver.find_element(By.NAME, "deletepost")
    driver.close()
    return 1

  except :
    driver.close()
    return 0

if __name__ == '__main__':
  print(test15())