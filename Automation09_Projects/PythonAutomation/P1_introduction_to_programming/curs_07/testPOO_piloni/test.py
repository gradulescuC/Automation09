from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()
chrome.implicitly_wait(5)
chrome.set_page_load_timeout(10)
chrome.get('https://formy-project.herokuapp.com/form')
chrome.find_element(By.TAG_NAME,'input').send_keys('Marian')
list= chrome.find_elements(By.TAG_NAME, 'input')
list[1].send_keys('Negru')
list[2].send_keys('Automation Testing')
chrome.find_element(By.ID,'radio-button-1').click()
chrome.find_element(By.CSS_SELECTOR,'input#checkbox-1').click()
select = Select(chrome.find_element(By.ID,'select-menu'))
select.select_by_visible_text("10+")
sleep(5)
chrome.quit()