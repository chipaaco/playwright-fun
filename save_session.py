from playwright.sync_api import sync_playwright


def save_session_manually():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.boot.dev/")

        print("Please log in using the browser window.")
        print("After logging in, press the Resume button in the Playwright inspector.")

        page.pause()

        context.storage_state(path="session_state.json")
        print("The session state file has been saved successfully.")

        browser.close()


if __name__ == "__main__":
    save_session_manually()
