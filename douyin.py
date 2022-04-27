from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def download(driver):
   try:
      time.sleep(1)                 
      driver.find_element_by_xpath('/html/body/main/section[2]/div/div/article/div[2]/div/a/span/span').click()
   except:
      return download(driver=driver)

linkez = open('link.txt','r',encoding='utf-8').read().splitlines()
driver = webdriver.Chrome()
for link in linkez:
    driver.get('https://snaptik.app/vn')
    time.sleep(1)
    driver.find_element_by_id('url').send_keys(link)
    time.sleep(1)
    driver.find_element_by_id('submiturl').click()
    download(driver=driver)
    time.sleep(5)
