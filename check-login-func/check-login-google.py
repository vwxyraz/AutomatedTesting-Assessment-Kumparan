from multiprocessing.connection import wait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
import time

PATH = "C:\selenium\chromedriver.exe"

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(PATH)
driver.get("https://kumparan.com")

popup = driver.find_element_by_id("onesignal-slidedown-cancel-button")
popup.click()

login = driver.find_element_by_xpath("//button[@data-qa-id='hd-login']")
login.click()

try:
    google = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@data-qa-id='btn-login-google']"))
    )
    google.click()
except:
    driver.quit()