from multiprocessing.connection import wait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time

PATH = "C:\selenium\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://kumparan.com/register")

user = "vyrafan@xmail.com"
passw = "12345678"

popup = driver.find_element_by_id("onesignal-slidedown-cancel-button")
popup.click()

login = driver.find_element_by_xpath("//button[@data-qa-id='hd-login']")
login.click()

try:
    email = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@data-qa-id='input-email']"))
    )
    email.send_keys(user)

    password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@data-qa-id='input-password']"))
        )
    password.send_keys(passw)

    driver.implicitly_wait(20)

    submit = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@data-qa-id='btn-save']"))
    )
    submit.click()
    time.sleep(3)

    eye = WebDriverWait(driver, 10).until(
         EC.presence_of_element_located((By.XPATH, "//div[@data-qa-id='right-add-on']"))
    )
    eye.click()

except:
    driver.quit()