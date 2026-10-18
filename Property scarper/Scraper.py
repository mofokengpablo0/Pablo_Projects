import time
import random
import pandas as pd
import undetected_chromedriver as uc
from bs4 import BeautifulSoup

# ================= CONFIGURATION =================
TARGET_URL = "https://www.property24.com/to-rent/johannesburg/gauteng/1?PropertyCategory=ApartmentOrFlat%2cTownhouse"
PAGES_TO_SCRAPE = 1
# =================================================


def scrape_property24():
    print("🚀 Starting Polished Johannesburg Scraper...")

    options = uc.ChromeOptions()
    driver = uc.Chrome(options=options)

    all_listings = []

    try:
        for page in range(1, PAGES_TO_SCRAPE + 1):
            url = (
                TARGET_URL.replace("/1?", f"/{page}?")
                if "/1?" in TARGET_URL
                else TARGET_URL
            )
            print(f"📄 Opening Page {page}: {url}")

            driver.get(url)
            time.sleep(15)

            soup = BeautifulSoup(driver.page_source, "html.parser")
            listings = soup.find_all("div", class_="js_resultTile")
            print(f"✅ Found {len(listings)} possible listings.")

            for item in listings:
                try:
                    # --- 1. CLEAN PRICE EXTRACTION ---
                    # First, try to find the hidden meta tag (the most accurate way)
                    price_meta = item.find("meta", itemprop="price")
                    if price_meta:
                        price_text = price_meta.get("content", "N/A")
                    else:
                        # Fallback: get only the first piece of text from the price div
                        price_tag = item.find("span", class_="p24_price") or item.find(
                            "div", class_="p24_price"
                        )
                        price_text = (
                            price_tag.get_text(strip=True).split("\n")[0]
                            if price_tag
                            else "N/A"
                        )

                    # --- 2. CLEAN TITLE EXTRACTION ---
                    title_tag = item.find("span", {"itemprop": "name"}) or item.find(
                        "div", class_="p24_description"
                    )
                    title_text = title_tag.get_text(strip=True) if title_tag else "N/A"

                    # --- 3. LOCATION ---
                    loc_tag = item.find("span", class_="p24_location")
                    location_text = loc_tag.get_text(strip=True) if loc_tag else "N/A"

                    # --- 4. ADDRESS ---
                    addr_tag = item.find("span", class_="p24_address")
                    address_text = addr_tag.get_text(strip=True) if addr_tag else "N/A"

                    # --- 5. ROOMS (BEDS) ---
                    bed_tag = item.find("span", {"title": "Bedrooms"})
                    if bed_tag:
                        bed_num = (
                            bed_tag.find("span").text.strip()
                            if bed_tag.find("span")
                            else "N/A"
                        )
                    else:
                        bed_num = "N/A"
                        if "Bedroom" in title_text:
                            bed_num = title_text.split("Bedroom")[0].strip()

                    # --- 6. URL ---
                    link_tag = item.find("a", href=True)
                    link = link_tag["href"] if link_tag else "N/A"
                    if link.startswith("/"):
                        link = "https://www.property24.com" + link

                    all_listings.append(
                        {
                            "Price": price_text,
                            "Rooms": bed_num,
                            "Title": title_text,
                            "Area": location_text,
                            "Address": address_text,
                            "URL": link,
                        }
                    )
                except Exception:
                    continue

        return all_listings

    finally:
        driver.quit()


# --- Execution and Saving ---
data = scrape_property24()

if data:
    df = pd.DataFrame(data)

    # Clean the Price column to ensure it's just a number
    # This removes everything that isn't a digit
    df["Price_Numeric"] = df["Price"].astype(str).str.replace(r"[^\d]", "", regex=True)
    df["Price_Numeric"] = pd.to_numeric(df["Price_Numeric"], errors="coerce")

    filename = "johannesburg_rentals_final.csv"
    df.to_csv(filename, index=False, encoding="utf-8")

    print("\n" + "=" * 40)
    print(f"✅ FINAL SUCCESS! Saved {len(df)} rentals to {filename}")
    print("=" * 40)
    print(df[["Price_Numeric", "Rooms", "Area", "Address"]].head())
else:
    print("\n❌ No data collected.")
