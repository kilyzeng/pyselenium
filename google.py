from time import sleep
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.google.com.hk/')
driver.find_element_by_id("lst-ib").clear()
driver.find_element_by_id('lst-ib').send_keys('python')
driver.find_element_by_name('btnK').click()
sleep(3)
driver.quit()
