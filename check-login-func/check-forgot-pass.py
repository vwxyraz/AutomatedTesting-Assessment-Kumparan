import email
from multiprocessing.connection import wait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time

PATH = "C:\selenium\chromedriver.exe"

user = "vyra@xmail.com"

driver = webdriver.Chrome(PATH)
driver.get("https://kumparan.com")

popup = driver.find_element_by_id("onesignal-slidedown-cancel-button")
popup.click()

login = driver.find_element_by_xpath("//button[@data-qa-id='hd-login']")
login.click()

try:
    btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@data-qa-id='btn-forgot-password']"))
    )
    btn.click()
    
    email = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@data-qa-id='input-email']"))
    )
    email.send_keys(user)

    submit = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@data-qa-id='btn-save']"))
    )
    submit.click()
except:
    driver.quit()