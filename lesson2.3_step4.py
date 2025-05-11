import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    # Инициализация браузера
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    # 1. Нажимаем на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # 2. Принимаем confirm
    alert = browser.switch_to.alert
    alert.accept()

    # 3. Решаем капчу на новой странице
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    # Вводим ответ
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(y)

    # Отправляем форму
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    # Получаем результат из alert
    time.sleep(10)

finally:
    # Завершаем работу
    time.sleep(5)
    browser.quit()
    