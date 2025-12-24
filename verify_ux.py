from playwright.sync_api import sync_playwright

def verify_final_state():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://localhost:8080")
        page.wait_for_load_state("networkidle")

        # 1. Verify Label Accessibility
        label = page.locator("label[for='emailInput']")

        # Check if label exists and has visually-hidden class
        if label.count() > 0:
            if "visually-hidden" in label.get_attribute("class"):
                print("✅ Accessibility: Visually hidden label found.")
            else:
                print("❌ Accessibility: Label found but missing visually-hidden class.")
        else:
            print("❌ Accessibility: Label not found.")

        # 2. Verify Inline Error Message (UX)
        # Disable browser validation so we can hit the JS logic
        page.evaluate("document.getElementById('emailForm').setAttribute('novalidate', 'true')")

        # Submit invalid email
        page.fill("#emailInput", "invalid-email")
        page.click("#submitBtn")

        # Check success message container for error text
        success_message = page.locator("#successMessage")

        # Wait for the message to be updated (it happens synchronously in JS but just in case)
        page.wait_for_timeout(500)

        text = success_message.text_content()
        classes = success_message.get_attribute("class")

        if "Please enter a valid email address" in text and "show" in classes:
            print("✅ UX: Inline error message displayed correctly.")
            page.screenshot(path="verification_success.png")
        else:
            print(f"❌ UX: Inline error message failed. Text: '{text}'")

        browser.close()

if __name__ == "__main__":
    verify_final_state()
