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

# news = driver.find_element_by_link_text("News")
# news.click()

trending = driver.find_elements_by_xpath("//div[@class='Viewweb__StyledView-sc-1ajfkkc-0 hlDrxP']")
# length = len(driver.find_elements_by_xpath("//div[@data-qa-id='trending-story-item']"))
for article in trending:
    article = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//div[@data-qa-id='trending-story-item']"))
    )
    article.click()
    time.sleep(3)
    driver.back()
    time.sleep(3)

# try:
#     # element = WebDriverWait(driver, 10).until(
#     #     EC.presence_of_element_located((By.LINK_TEXT, "News"))
#     # )
#     # element.click()
#     # time.sleep(5)
#     length = len(driver.find_elements_by_xpath("//*[@data-qa-id='trending-story-item']"))
#     count = 0

#     while (count < length):
#         trending = driver.find_elements_by_xpath("//*[@data-qa-id='trending-story-item']")
#         trending[count].click()
#         time.sleep(5)
#         driver.back()

#     # trending = driver.find_elements_by_xpath("//button[@data-qa-id='trending-story-item']")
#     # for article in trending:
#     #     article = driver.find_element_by_class_name("LabelLinkweb__StyledLink-fupmuj-0 kZWIkp")
#     #     article.click()
#     #     time.sleep(5)
#     #     driver.back()

# except:
#     driver.quit()
