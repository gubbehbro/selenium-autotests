import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Ожидаем, пока в элементе с id="price" не появится текст "$100"
    # Ждем не менее 12 секунд, как указано в задании
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # 2. Нажимаем кнопку "Book"
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    # 3. Решаем математическую задачу
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    # 4. Вводим ответ и отправляем форму
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    solve_button = browser.find_element(By.ID, "solve")
    solve_button.click()

finally:
    # Оставляем время, чтобы успеть скопировать результат из всплывающего окна
    time.sleep(10)
    browser.quit()
