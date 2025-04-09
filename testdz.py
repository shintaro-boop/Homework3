from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()
browser.maximize_window()
sbis_site = 'https://saby.ru/'
try:
    browser.get(sbis_site)
    sleep(2)
    assert browser.current_url == sbis_site, 'Неверно открыт сайт'
    start_btn = browser.find_element(By.CSS_SELECTOR, '.sbisru-Button--primary')
    start_btn.click()
    sleep(3)
    handles = browser.window_handles
    browser.switch_to.window(handles[1])
    current_date = datetime.now()
    date = current_date.strftime('%Y-%m-%d')
    login = browser.find_element(By.CSS_SELECTOR, f'[name="ws-input_{date}"]')
    sleep(7)
    login.send_keys('my_login')
    sleep(7)
    login.clear()
    sleep(7)
finally:
    browser.quit()