from playwright.sync_api import sync_playwright


def verify_saved_session():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        context = browser.new_context(storage_state="session_state.json")
        page = context.new_page()

        page.goto("https://www.boot.dev/lessons/78b4646f-85aa-42c7-ba46-faec2f0902a9")

        print("If the session loaded correctly, you should see your user dashboard.")

        page.wait_for_timeout(5000)

        browser.close()


if __name__ == "__main__":
    verify_saved_session()
