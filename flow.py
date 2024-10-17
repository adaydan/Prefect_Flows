from prefect import flow, task
from playwright.sync_api import sync_playwright
import subprocess
global page
    

@flow(log_prints=True)
def launch_browser():
    print('starting...')
    subprocess.run(["playwright", "install", "chrome"], check=False)
    with sync_playwright() as p:
        # Launch Chrome (non-headless)
        browser = p.chromium.launch(headless=True, channel="chrome")

        # Open a new browser page
        page = browser.new_page()

        page.goto("https://webscraper.io/test-sites")
        x = [i.text_content() for i in page.query_selector_all('.site-heading a')]
        print(x)
        print('_______________')
        for i in x:
            print(i)
        print('_______________')

        browser.close()
