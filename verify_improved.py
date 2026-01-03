from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8080")

        # Click submit with invalid email
        page.fill("#emailInput", "invalid-email")
        page.click("#submitBtn")

        # Wait for error message to appear
        page.wait_for_selector("#successMessage.show", state="visible", timeout=3000)

        # Verify text content
        error_msg = page.text_content("#successMessage")
        print(f"Error message: {error_msg}")

        if "Please enter a valid email address" in error_msg:
             print("SUCCESS: Error message displayed inline.")
        else:
             print("FAILURE: Unexpected error message.")

        # Take screenshot
        page.screenshot(path="verification_improved.png")

        browser.close()

if __name__ == "__main__":
    run()
