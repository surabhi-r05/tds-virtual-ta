import asyncio
from playwright.async_api import async_playwright

BASE_URL = "https://tds.s-anand.net/#/"

# Add important sub-pages
PAGES = [
    "",  # homepage
    "docker",
    "postgres",
    "markdown",
    "discourse",
    "python",
    "airflow",
    "projects",
    "evaluation",
    "faq"
]

async def scrape_page(playwright, slug):
    url = BASE_URL + slug
    browser = await playwright.chromium.launch(headless=True)
    page = await browser.new_page()
    await page.goto(url)
    await page.wait_for_timeout(1000)  # wait for JS to load

    content = await page.inner_text("main")  # assumes content inside <main>
    await browser.close()
    return slug or "index", content.strip()

async def scrape_all():
    results = {}
    async with async_playwright() as playwright:
        for slug in PAGES:
            key, content = await scrape_page(playwright, slug)
            results[key] = content
    return results

if __name__ == "__main__":
    data = asyncio.run(scrape_all())
    for k, v in data.items():
        print(f"\n=== {k.upper()} ===\n")
        print(v[:1000], "...\n")  # preview only
