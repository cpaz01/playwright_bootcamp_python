from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://playwright.dev/')
    page.screenshot(path='example.png')
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
