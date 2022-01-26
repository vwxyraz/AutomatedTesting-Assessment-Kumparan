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
driver.get("https://kumparan.com/create-password?email=vyrrra%40gmail.com&token=EgHNOgIRty")

passw = "vyrafan"
passu = "vyrafan"

popup = driver.find_element_by_id("onesignal-slidedown-cancel-button")
popup.click()

# login = driver.find_element_by_xpath("//button[@data-qa-id='hd-login']")
# login.click()

try:
    password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))
    )
    password.send_keys(passw)
    
    ulang = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='confirm-password']"))
    )
    ulang.send_keys(passu)

    driver.implicitly_wait(20)

    submit = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@data-qa-id='btn-save']"))
    )
    submit.click()



except:
    driver.quit()