# Прописываем в терминале:
# python -m pip install --upgrade pip (Обновление менеджера пакетов pip)
# pip install selenium (Устанавливаем библиотеку selenium)
# pip install webdriver-manager (Устанавливаем webdriver-manager)
import time

# импортируем необходимые библиотеки и элементы
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# создаем и настраиваем экземпляр driver класса webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
# options.add_argument('--headless')
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

# создаем переменную содержащую базовую ссылку и открываем её с помощью созданного ранее driver
base_url = 'http://demoqa.com/checkbox'
driver.get(base_url)
driver.maximize_window()

#создаем переменную для чек-бокса, нажимаем его и проверяем нажатие
check_box = driver.find_element(By.XPATH, "//span[@class='rct-checkbox']")
check_box.click()
check_box.is_selected()
print('Чек-бокс выбран')
