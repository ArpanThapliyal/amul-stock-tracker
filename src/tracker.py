from playwright.sync_api import sync_playwright

URL = "https://shop.amul.com/en/product/amul-high-protein-buttermilk-200-ml-or-pack-of-30"
PINCODE = "121010"


def is_in_stock() -> bool:
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        page.goto(
            URL,
            wait_until="domcontentloaded",
            timeout=60000
        )
        # ---------- DEBUG ----------
        page.screenshot(path="page.png", full_page=True)

        with open("page.html", "w", encoding="utf-8") as f:
            f.write(page.content())
        # ---------------------------


        pin_input = page.get_by_placeholder(
            "Enter Your Pincode"
        )

        pin_input.wait_for(timeout=15000)

        pin_input.fill(PINCODE)

        page.wait_for_timeout(2000)

        pin_input.press("Enter")

        page.wait_for_timeout(8000)

        alerts = page.locator(
            "div.alert.alert-danger"
        )

        is_sold_out = False

        for i in range(alerts.count()):

            text = alerts.nth(i).inner_text().strip()

            if text == "Sold Out":
                is_sold_out = True
                break

        browser.close()

        return not is_sold_out