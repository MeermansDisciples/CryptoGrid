from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.bigparser.com/grids")
assert "BigParser" in driver.title
"""elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)"""
loginName = driver.find_element_by_name('email')
loginName.send_keys('meermansdisciples@gmail.com')
loginPass = driver.find_element_by_name('pass')
loginPass.send_keys('meergoat')
loginBtn = driver.find_element_by_class_name('login-btn')
loginBtn.click()
driveButton = driver.find_element_by_xpath('/html/body/div[1]/ui-view/div[5]/div[3]/div/div[1]/div[2]/ul/li[1]/img')
driveButton.click()
searchButton = drive.find_element_by_xpath('/html/body/div[1]/ui-view/div[2]/div/div/div[2]/a[3]')
searchButton.click()
syncBtn = drive.find_element_by_xpath('/html/body/div[1]/ui-view/div[2]/div/div/div[2]/a[2]')
syncBtn.click()
assert "No results found." not in driver.page_source
driver.close()
