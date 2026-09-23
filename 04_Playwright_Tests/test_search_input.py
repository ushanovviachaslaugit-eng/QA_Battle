# test_search_input.py — Задание №15 (версия для Google)

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # 1. Переходим на Google
    page.goto("https://www.google.com")

    # 2. ЖДЁМ, пока поле поиска появится
    page.wait_for_selector("textarea[name='q']", timeout=10000)

    # 3. Вводим текст
    page.fill("textarea[name='q']", "Погода в Минске")

    # 4. Ждём 3 секунды
    page.wait_for_timeout(3000)

    browser.close()