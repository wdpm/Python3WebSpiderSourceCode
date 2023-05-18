from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
# input_first = browser.find_element_by_id('q')
input_first = browser.find_element(by=By.ID,value='q')
# input_second = browser.find_element_by_css_selector('#q')
# input_third = browser.find_element_by_xpath('//*[@id="q"]')
print(input_first)
# print(input_first, input_second, input_third)
browser.close()