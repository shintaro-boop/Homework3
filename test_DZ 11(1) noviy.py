
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()
browser.maximize_window()
sbis_site = 'https://saby.ru/'
tensor_site = 'https://tensor.ru/about'
try:
    browser.get(sbis_site)
    sleep(2)
    assert browser.current_url == sbis_site, 'Неверно открыт сайт'
    contacts = browser.find_elements(By.CSS_SELECTOR, '.sbisru-Header__menu-link')
    for contact in contacts:
        if contact.text == "Контакты":
            contact.click()
        pass
    sleep(3)
    perexod = browser.find_element(By.CSS_SELECTOR, '.sbisru-Header-ContactsMenu__arrow-icon')
    perexod.click()
    sleep(10)
    logo = browser.find_element(By.CSS_SELECTOR, '[alt ="Разработчик системы Saby — компания «Тензор»"]')
    logo.click()
    sleep(10)
    handles = browser.window_handles
    browser.switch_to.window(handles[1])
    sleep(3)
    strong = browser.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content')
    browser.execute_script("return arguments[0].scrollIntoView({block: 'end', inline: 'nearest'});", strong)
    assert strong.is_displayed(), 'Блок не отображается'
    podrobnee = strong.find_element(By.CSS_SELECTOR, '.tensor_ru-link.tensor_ru-Index__link')
    podrobnee.click()
    sleep(7)
    assert browser.current_url == tensor_site, 'Неверно открыт сайт'



finally:
    browser.quit()



