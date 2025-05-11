from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try:
    # Инициализация браузера
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    # Заполняем текстовые поля
    browser.find_element(By.NAME, "firstname").send_keys("Иван")
    browser.find_element(By.NAME, "lastname").send_keys("Петров")
    browser.find_element(By.NAME, "email").send_keys("test@example.com")

    # Создаем временный файл для загрузки
    with open("testfile.txt", "w") as file:
        file.write("Это тестовый файл")

    # Загружаем файл
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "testfile.txt")
    browser.find_element(By.ID, "file").send_keys(file_path)

    # Нажимаем кнопку Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Получаем результат из alert
    time.sleep(10)

finally:
    # Удаляем временный файл и закрываем браузер
    time.sleep(5)
    if os.path.exists("testfile.txt"):
        os.remove("testfile.txt")
    browser.quit()