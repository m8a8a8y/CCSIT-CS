from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load local file
        filepath = os.path.abspath("labs.html")
        page.goto(f"file://{filepath}")

        # Verify Title
        print(f"Page Title: {page.title()}")

        # Verify Navigation Link
        labs_link = page.query_selector("nav a[href='labs.html']")
        if labs_link:
            print("LABS link found in navigation.")
        else:
            print("ERROR: LABS link NOT found.")

        # Verify Challenge Cards
        cards = page.query_selector_all(".lab-card")
        print(f"Found {len(cards)} challenge cards.")

        for i, card in enumerate(cards):
            title = card.query_selector("h3").inner_text()
            print(f"Card {i+1}: {title}")

        # Take Screenshot
        page.screenshot(path="verification/labs_page.png", full_page=True)
        print("Screenshot saved to verification/labs_page.png")

        browser.close()

if __name__ == "__main__":
    run()
