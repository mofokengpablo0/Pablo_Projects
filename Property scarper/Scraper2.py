import time
import random
import pandas as pd
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
import re

# ================= CONFIGURATION =================
# I have used your specific Johannesburg filtered URL here
# Note: I changed the '100' to '1' so the scraper starts at the first page.
TARGET_URL = "https://www.property24.com/to-rent/johannesburg/gauteng/1?PropertyCategory=ApartmentOrFlat%2cTownhouse"
PAGES_TO_SCRAPE = 3  # Set this to how many pages you want to collect
# =================================================


def scrape_property24():
    print("🚀 Starting Johannesburg Rental Scraper...")

    options = uc.ChromeOptions()
    # options.add_argument("--headless") # Run in background
    driver = uc.Chrome(options=options)

    all_listings = []

    try:
        for page in range(1, PAGES_TO_SCRAPE + 1):
            # Logic to handle your specific URL:
            # It replaces the '/1' (or whatever number is there) with the current page number
            # while keeping the ?PropertyCategory filter.
            url = (
                TARGET_URL.replace("/1?", f"/{page}?")
                if "/1?" in TARGET_URL
                else (
                    TARGET_URL.replace("/100?", f"/{page}?")
                    if "/100?" in TARGET_URL
                    else TARGET_URL.replace("/1", f"/{page}")
                )
            )  # Fallback

            print(f"📄 Scraping Page {page}: {url}")

            driver.get(url)

            # Important: Random sleep to prevent bot detection
            time.sleep(random.uniform(6, 11))

            soup = BeautifulSoup(driver.page_source, "html.parser")
            listings = soup.find_all("div", class_="teaser-item")

            if not listings:
                print(
                    f"⚠️ No listings found on page {page}. You might be blocked or reached the end."
                )
                break

            for item in listings:
                try:
                    # 1. PRICE
                    price_meta = item.find("meta", itemprop="priceCurrency")
                    price_text = (
                        price_meta.parent.get_text(strip=True) if price_meta else "N/A"
                    )

                    # 2. TITLE & ROOMS
                    title_tag = item.find("span", {"itemprop": "name"})
                    title_text = title_tag.text.strip() if title_tag else "N/A"

                    if "Bedroom" in title_text:
                        parts = title_text.split("Bedroom")
                        rooms = parts[0].strip()
                        prop_type = parts[1].strip()
                    else:
                        rooms = "N/A"
                        prop_type = title_text

                    # 3. GENERAL LOCATION
                    location_tag = item.find("span", class_="p24_location")
                    location_text = location_tag.text.strip() if location_tag else "N/A"

                    # 4. SPECIFIC ADDRESS
                    address_tag = item.find("span", class_="p24_address")
                    address_text = address_tag.text.strip() if address_tag else "N/A"

                    # 5. PROPERTY LINK
                    link_tag = item.find("a", href=True)
                    link = link_tag["href"] if link_tag else "N/A"
                    if link.startswith("/"):
                        link = "https://www.property24.com" + link

                    all_listings.append(
                        {
                            "Price": price_text,
                            "Rooms": rooms,
                            "Property Type": prop_type,
                            "Area": location_text,
                            "Street Address": address_text,
                            "Full Title": title_text,
                            "URL": link,
                        }
                    )
                except Exception as e:
                    print(f"⚠️ Error parsing a listing: {e}")

        return all_listings

    finally:
        driver.quit()


# --- Execution and Saving ---
data = scrape_property24()

if data:
    df = pd.DataFrame(data)

    # BONUS: Clean Price into a number for sorting in Excel
    # This removes 'R' and spaces and converts to an actual number
    df["Price_Numeric"] = df["Price"].str.replace(r"[^\d]", "", regex=True)
    df["Price_Numeric"] = pd.to_numeric(df["Price_Numeric"], errors="coerce")

    filename = "johannesburg_rentals.csv"
    df.to_csv(filename, index=False, encoding="utf-8")

    print("\n" + "=" * 40)
    print(f"✅ DONE! Found {len(df)} rentals.")
    print(f"📁 Saved to: {filename}")
    print("=" * 40)
    print(df[["Price", "Rooms", "Area", "Street Address"]].head())
else:
    print("\n❌ No data collected.")
