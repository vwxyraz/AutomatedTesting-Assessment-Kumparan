from lib2to3.pgen2 import driver
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

comments = "This article is  really helpful and insightful with accurate data from the officials. There's no spelling or grammar error, and how it written is interesting. Thanks for the reporter, writer, and editor's works"
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(PATH)
driver.get("https://kumparan.com/kumparansains/musim-hujan-waspada-nyamuk-demam-berdarah-1xN03hFo4Uw")

time.sleep(3)
popup = driver.find_element_by_id("onesignal-slidedown-cancel-button")
popup.click()

# article = WebDriverWait(driver, 30).until(
#         EC.presence_of_element_located((By.XPATH, "//div[@data-qa-id='trending-story-item']"))
#     )
# article.click()

comment = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//button[@data-qa-id='btn-comment']"))
    )
comment.click()
driver.implicitly_wait(5)
# class='CommentEditorweb__EditorBorder-sc-1tnt9hh-0 dXNXZI'
# data-qa-id='input-comment'

# input = WebDriverWait(driver, 30).until(
#     EC.presence_of_element_located((By.XPATH, "//div[@class='CommentEditorweb__EditorBorder-sc-1tnt9hh-0 dXNXZI']"))
# )
# input.send_keys("haha")

# driver.implicitly_wait(5)

# submit = WebDriverWait(driver, 30).until(
#     EC.presence_of_element_located((By.XPATH, "//button[@data-qa-id='btn-send-comment']"))
# )
# submit.click()

try:
    input = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//div[@data-qa-id='input-comment']"))
    )
    input.send_keys("")

    driver.implicitly_wait(5)

    submit = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//button[@data-qa-id='btn-send-comment']"))
    )
    submit.click()

except:
    driver.quit()