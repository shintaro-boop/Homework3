from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


browser = webdriver.Chrome()
sbis_site = 'https://saby.ru/'
try:
    browser.get(sbis_site)
    sleep(3)
    assert browser.current_url == sbis_site, 'Неверно открыт сайт'
    sleep(3)
    news_item = browser.find_element(By.CSS_SELECTOR, '.sbisru-h5.sbisru-Main-news')
    sleep(3)
    browser.execute_script("return arguments[0].scrollIntoView({block: 'end', inline: 'nearest'});", news_item)
    sleep(3)
    news_item.click()
    sleep(3)
finally:
    browser.quit()