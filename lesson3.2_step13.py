import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_registration1(self):
        self.browser.get("http://suninjuly.github.io/registration1.html")

        # Заполняем обязательные поля
        self.browser.find_element_by_css_selector(".first_block .first").send_keys("Ivan")
        self.browser.find_element_by_css_selector(".first_block .second").send_keys("Petrov")
        self.browser.find_element_by_css_selector(".first_block .third").send_keys("test@test.com")

        # Отправляем форму
        self.browser.find_element_by_css_selector("button.btn").click()

        # Проверяем результат
        welcome_text = self.browser.find_element_by_tag_name("h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_registration2(self):
        self.browser.get("http://suninjuly.github.io/registration2.html")

        # Пытаемся заполнить обязательные поля (должно вызвать NoSuchElementException)
        self.browser.find_element_by_css_selector(".first_block .first").send_keys("Ivan")
        self.browser.find_element_by_css_selector(".first_block .second").send_keys("Petrov")
        self.browser.find_element_by_css_selector(".first_block .third").send_keys("test@test.com")

        # Отправляем форму
        self.browser.find_element_by_css_selector("button.btn").click()

        # Проверяем результат
        welcome_text = self.browser.find_element_by_tag_name("h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    unittest.main()