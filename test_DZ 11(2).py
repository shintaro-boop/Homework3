import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException



chrome_options = Options()
chrome_options.add_argument("--disable-notifications")



browser = webdriver.Chrome(options=chrome_options)
browser.maximize_window()
sbis_site = 'https://fix-online.saby.ru/'
try:
    # Открываем сайт
    browser.get(sbis_site)
    sleep(2)
    current_date = datetime.now()
    date = current_date.strftime('%Y-%m-%d')
    login = browser.find_element(By.CSS_SELECTOR, f'[name="ws-input_{date}"]')
    sleep(7)
    login.send_keys('shintaro', Keys.ENTER)
    password = browser.find_element(By.CSS_SELECTOR, f'[name="ws-input_{date}"][type = "password"]')
    sleep(7)
    password.send_keys('Test123', Keys.ENTER)
    sleep(15)
    contacts = browser.find_element(By.CSS_SELECTOR, '.NavigationPanels-Accordion__container a:nth-child(2)')
    contacts.click()
    sleep(10)
    contacts1 = browser.find_element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle.NavigationPanels-SubMenu__title-with-separator.NavigationPanels-Accordion__prevent-default')
    contacts1.click()
    sleep(7)
    plus = browser.find_element(By.CSS_SELECTOR, '.controls-icon_size-m.controls-BaseButton__icon.icon-RoundPlus.controls-icon')
    plus.click()
    sleep(3)
    poisk = browser.find_element(By.CSS_SELECTOR, f'[name="ws-input_{date}"][type = "text"]')
    sleep(3)
    poisk.send_keys('Баранов Вадим Игоревчи')
    sleep(3)
    vibor = browser.find_element(By.CSS_SELECTOR, '[data-qa="person-Information__fio"][title="Баранов Вадим Игоревчи"]')
    vibor.click()
    sleep(3)
    messages = browser.find_element(By.CSS_SELECTOR, '[data-slate-node="element"]')
    sleep(3)
    messages.send_keys('Свой первый автотест')
    sleep(3)
    actions = ActionChains(browser)
    actions.key_down(Keys.CONTROL).send_keys(Keys.RETURN).key_up(Keys.CONTROL).perform()
    sleep(3)
    msgproverka = browser.find_element(By.CSS_SELECTOR, '[data-qa="msg-dialogs-item__addressee"][title="Баранов Вадим Игоревчи"]')
    assert msgproverka.is_displayed(), "Элемент не найден или не отображается!"
    actions = ActionChains(browser)
    actions.move_to_element(msgproverka).perform()
    sleep(1)
    checkbox = browser.find_element(By.CSS_SELECTOR, '.controls-CheckboxMarker__state-null__icon-color__transparent')
    checkbox.click()
    sleep(3)
    try :
        checkbox1 = browser.find_element(By.CSS_SELECTOR, '.controls-CheckboxMarker__state-null__icon-color__enabled')
        checkbox1.click()
        checkbox1.click()
        sleep(3)
        checkbox2 = browser.find_element(By.CSS_SELECTOR,'.controls-icon_size-s.controls-BaseButton__icon.icon-Erase.controls-icon')
        checkbox2.click()
        sleep(10)
        msgproverka = browser.find_element(By.CSS_SELECTOR,'[data-qa="msg-dialogs-item__addressee"][title="Баранов Вадим Игоревчи"]')
        assert not msgproverka.is_displayed(), "Элемент найден и отображается!"
        sleep(3)
        print ('Элемент удален. Завершаем выполнение...')
        sleep(7)
        sys.exit()
    except NoSuchElementException:
        print("Видимо у вас больше чем 1 сообщение. Выполнение продолжается...")
    sleep(3)
    checkbox2 = browser.find_element(By.CSS_SELECTOR, '.controls-icon_size-s.controls-BaseButton__icon.icon-Erase.controls-icon')
    checkbox2.click()
    sleep(10)
    try:
        msgproverka = browser.find_element(By.CSS_SELECTOR,
                                           '[data-qa="msg-dialogs-item__addressee"][title="Баранов Вадим Игоревчи"]')
        assert msgproverka.is_displayed(), "Элемент найден и отображается!"
    except NoSuchElementException:
        print("Элемент успешно удалён!")


finally:
    browser.quit()