from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8080")

        # Take a screenshot to verify page load
        page.screenshot(path="baseline_load.png")

        # Define handler
        def handle_dialog(dialog):
            print(f"Dialog opened: {dialog.message}")
            dialog.dismiss()

        page.on("dialog", handle_dialog)

        # Click submit with invalid email
        page.fill("#emailInput", "invalid-email")
        page.click("#submitBtn")

        # Wait a bit
        page.wait_for_timeout(2000)

        browser.close()

if __name__ == "__main__":
    run()
