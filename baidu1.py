# from time import sleep
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com')
# driver.find_element_by_id('kw').clear()
# driver.find_element_by_id('kw').send_keys('python')
# sleep(2)
# driver.find_element_by_name('su').click()
# driver.quit()


# from selenium import webdriver
# from time import sleep
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
#
# driver.find_element_by_id("kw").clear()
# driver.find_element_by_i/d("kw").send_keys("selenium")
# driver.find_element_by_id("su").click()
# sleep(3)
# driver.quit()

# from time import sleep
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
# driver.find_element_by_name("wd").clear()
# driver.find_element_by_name("wd").send_keys("python")
# sleep(3)
# driver.find_element_by_id("su").click()
# sleep(4)
# driver.quit()

# from .firefox.webdriver import WebDriver as Firefox
#from selenium.webdriver import Firefox
from time import sleep
from selenium import webdriver
driver = webdriver.Firefox()
driver.get('https://www.baidu.com')
driver.find_element_by_name("wd").clear()
driver.find_element_by_name("wd").send_keys("python")
sleep(3)
driver.find_element_by_id("su").click()
sleep(4)
driver.quit()

