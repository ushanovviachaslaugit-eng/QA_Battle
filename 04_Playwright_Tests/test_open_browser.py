# test_open_browser.py — Задание №14
# Первый запуск браузера через Playwright

from playwright.sync_api import sync_playwright

# 1. Открываем "контекст" Playwright (это как пульт управления браузером)
with sync_playwright() as p:
    # 2. Запускаем браузер Chrome (headless=False — чтобы увидеть окно)
    browser = p.chromium.launch(headless=False)

    # 3. Создаём новую вкладку (страницу)
    page = browser.new_page()

    # 4. Переходим на сайт
    # page.goto("https://yandex.ru")
    page.goto("https://google.com")

    # 5. Выводим заголовок страницы в консоль
    print("Заголовок страницы:", page.title())

    # 6. Ждём 2 секунды, чтобы увидеть результат
    page.wait_for_timeout(2000)

    # 7. Закрываем браузер
    browser.close()

print("Программа завершена!")