from multiprocessing.connection import wait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time

PATH = "C:\selenium\chromedriver.exe"

hp = "081111222333"

driver = webdriver.Chrome(PATH)
driver.get("https://kumparan.com")

popup = driver.find_element_by_id("onesignal-slidedown-cancel-button")
popup.click()

login = driver.find_element_by_xpath("//button[@data-qa-id='hd-login']")
login.click()

try:
    phone = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@data-qa-id='btn-login-phone']"))
    )
    phone.click()

    noph = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@data-qa-id='input-phone-number']"))
    )
    noph.send_keys(hp)
    noph.send_keys(Keys.RETURN)

    lanjut = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@data-qa-id='btn-submit-login-phone']"))
    )
    lanjut.click()

    ulang = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@data-qa-id='btn-resend-otp']"))
    )
    ulang.click()

except:
    driver.quit()