
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


download_dir = os.path.abspath(r"C:\Users\inumaki\PycharmProjects\Homework3")
chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": download_dir,  # Указываем папку для загрузки файлов
    "download.prompt_for_download": False,  # Отключаем запрос "Сохранить файл"
    "download.directory_upgrade": True,  # Разрешаем изменение настроек загружаемого файла
    "safebrowsing.enabled": True  # Отключаем предупреждения браузера
}
chrome_options.add_experimental_option("prefs", prefs)

browser = webdriver.Chrome(options=chrome_options)
browser.maximize_window()
sbis_site = 'https://saby.ru/'
tensor_site = 'https://tensor.ru/about'
try:
    browser.get(sbis_site)

    sleep(2)

    assert browser.current_url == sbis_site, 'Неверно открыт сайт'
    supports = browser.find_elements(By.CSS_SELECTOR, '.sbisru-Header__menu-link')
    for support in supports:
        if support.text == "Поддержка":
            support.click()
        pass

    sleep(5)

    download = browser.find_element(By.CSS_SELECTOR, 'a[href*="/download?tab=plugin&innerTab=default"]')
    browser.execute_script("return arguments[0].scrollIntoView({block: 'end', inline: 'nearest'});", download)
    assert download.is_displayed(), 'Блок не отображается'
    download.click()

    sleep(10)

    filedonwload = browser.find_element(By.CSS_SELECTOR, 'a[href*="https://update.saby.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe"]')
    browser.execute_script("return arguments[0].scrollIntoView({block: 'end', inline: 'nearest'});", filedonwload)
    filedonwload.click()

    sleep(10)

    def is_file_downloaded(folder, file_name, timeout=30):
        elapsed_time = 0
        c = 0
        while elapsed_time < timeout:
            if file_name in os.listdir(folder):  # Проверяем наличие файла
                return True
            sleep(1)
            elapsed_time += 1
            file_name = f"sbisplugin-setup-web.exe"
        return False
    expected_file_name = "sbisplugin-setup-web.exe"
    if is_file_downloaded(download_dir, expected_file_name):
        file_path = os.path.join(download_dir, expected_file_name)
        file_size = os.path.getsize(file_path)
        file_size_kb = file_size / 1024  # Конвертация в килобайты
        file_size_mb = file_size_kb / 1024
        print(f"Файл скачался успешно. Размер: {file_size_mb:.2f} байт.")
        os.remove(file_path)
    else:
        print("Файл не скачался.")
finally:
    browser.quit()


