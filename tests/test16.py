from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def test16(randomgroupname1: str, randomgroupname2: str):
  driver = webdriver.Chrome()
  driver.get(r"http://127.0.0.1:5000")
  time.sleep(1)

  # press signup button
  signup = driver.find_element(By.NAME, "stablishbutton")
  signup.click()
  time.sleep(2)

  group = Select(driver.find_element(By.NAME, 'groupname'))
  account = driver.find_element(By.ID, "username")
  password = driver.find_element(By.ID, "password")
  group.select_by_visible_text(randomgroupname1)
  time.sleep(1)
  account.send_keys("billy")
  time.sleep(1)
  password.send_keys("billy")
  time.sleep(1)

  create = driver.find_element(By.NAME, 'establish')
  create.click()
  time.sleep(1)

  back = driver.find_element(By.NAME, 'backtologin')
  back.click()
  time.sleep(1)

  # press signup button again
  signup = driver.find_element(By.NAME, "stablishbutton")
  signup.click()
  time.sleep(2)

  group = Select(driver.find_element(By.NAME, 'groupname'))
  account = driver.find_element(By.ID, "username")
  password = driver.find_element(By.ID, "password")
  group.select_by_visible_text(randomgroupname2)
  time.sleep(1)
  account.send_keys("billy")
  time.sleep(1)
  password.send_keys("billy")
  time.sleep(1)

  create = driver.find_element(By.NAME, 'establish')
  create.click()
  time.sleep(1)

  back = driver.find_element(By.NAME, 'backtologin')
  back.click()
  time.sleep(1)

  # login grouptwo
  group = Select(driver.find_element(By.NAME, 'groupname'))
  account = driver.find_element(By.ID, "username")
  password = driver.find_element(By.ID, "password")
  group.select_by_visible_text(randomgroupname2)
  time.sleep(1)
  account.send_keys("billy")
  time.sleep(1)
  password.send_keys("billy")
  time.sleep(1)

  # press login button
  login = driver.find_element(By.NAME, "loginbutton")
  login.click()
  time.sleep(2)

  try:
    driver.find_element(By.NAME, 'logout')
    driver.close()
    return 0
  except:
    driver.close()
    return 1


