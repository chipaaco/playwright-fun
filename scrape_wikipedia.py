import asyncio
from playwright.async_api import async_playwright

WIKI_URL = "https://en.wikipedia.org/wiki/Web_scraping"


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(WIKI_URL)

        # Seleccionar el primer párrafo debajo del título del artículo
        first_paragraph_locator = (
            "div#mw-content-text .mw-parser-output > p:not(:empty)"
        )
        first_paragraph = await page.locator(
            first_paragraph_locator
        ).first.text_content()

        print("Primer párrafo extraído:")
        print(first_paragraph.strip())

        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
