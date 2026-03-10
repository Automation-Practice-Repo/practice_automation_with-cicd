from playwright.sync_api import sync_playwright

def test_open_page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("https://the-internet.herokuapp.com/login")

        assert "The Internet" in page.title()

        browser.close()

from playwright.sync_api import sync_playwright
from ci_cd_game.pages.login_page import LoginPage

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("https://the-internet.herokuapp.com/login")

        login = LoginPage(page)
        login.login("tomsmith", "SuperSecretPassword!")

        assert "Secure Area" in page.content()

        browser.close()