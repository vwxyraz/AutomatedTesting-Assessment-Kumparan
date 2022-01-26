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
driver.get("https://kumparan.com/")

popup = driver.find_element_by_id("onesignal-slidedown-cancel-button")
popup.click()

article = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//div[@data-qa-id='trending-story-item']"))
    )
article.click()

share = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//a[@class='sc-1d6h4x8-0 ftTAzK track_share_button']"))
    )
# driver.find_element_by_xpath("//a[@class='sc-1d6h4x8-0 ftTAzK track_share_button']")
share.click()
time.sleep(3)

try:
    wa = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//button[@data-qa-id='share-whatsapp']"))
    )
    wa.click()
    time.sleep(3)
    parent = driver.current_window_handle

    uselessWindows = driver.window_handles
    driver.switch_to.window(uselessWindows[-1])
    time.sleep(3)
    driver.close()
    driver.switch_to.window(uselessWindows[0])

    share.click()
    time.sleep(3)

    fb = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//button[@data-qa-id='share-fb']"))
    )
    fb.click()
    time.sleep(3)
    parent = driver.current_window_handle

    uselessWindows = driver.window_handles
    driver.switch_to.window(uselessWindows[-1])
    time.sleep(3)
    driver.close()
    driver.switch_to.window(uselessWindows[0])

    share.click()
    time.sleep(3)

    twt = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//button[@data-qa-id='share-twitter']"))
    )
    twt.click()
    time.sleep(3)
    parent = driver.current_window_handle

    uselessWindows = driver.window_handles
    driver.switch_to.window(uselessWindows[-1])
    time.sleep(3)
    driver.close()
    driver.switch_to.window(uselessWindows[0])

    share.click()
    time.sleep(3)

    line = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//button[@data-qa-id='share-line']"))
    )
    line.click()
    time.sleep(3)
    parent = driver.current_window_handle

    uselessWindows = driver.window_handles
    driver.switch_to.window(uselessWindows[-1])
    time.sleep(3)
    driver.close()
    driver.switch_to.window(uselessWindows[0])

    share.click()
    time.sleep(3)

    url = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//button[@data-qa-id='share-copy-clipboard']"))
    )
    url.click()

except:
    driver.quit()