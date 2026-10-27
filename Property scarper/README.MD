
***

# 🏠 Property24 Rental Scraper

A professional-grade Python web scraper designed to extract rental listing data from Property24. This tool bypasses advanced bot detection and handles dynamic content to provide a clean, sortable dataset of available properties.

## 🎯 Project Overview
The goal of this project was to automate the collection of rental data for Apartments and Townhouses in Johannesburg. The scraper navigates the website, handles JavaScript rendering, and extracts key data points into a CSV file for market analysis.

### 📊 Data Collected
- **Price:** Cleaned numeric value for sorting.
- **Rooms:** Number of bedrooms.
- **Property Type:** (e.g., Apartment, Townhouse).
- **Area:** The suburb or general location.
- **Address:** The specific street address (where available).
- **URL:** Direct link to the listing.

---

## 🛠️ Technical Stack
- **Language:** Python 3.12
- **Browser Automation:** `undetected-chromedriver` (Bypasses Cloudflare/Bot detection).
- **HTML Parsing:** `BeautifulSoup4`.
- **Data Engineering:** `Pandas` (For data cleaning and CSV export).
- **Driver Management:** `webdriver-manager` (Automates ChromeDriver installation).

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have [Python 3.12+](https://www.python.org/downloads/) and [Google Chrome](https://www.google.com/chrome/) installed.

### 2. Installation
It is highly recommended to use a virtual environment to avoid dependency conflicts.

```bash
# Create a virtual environment
python -m venv .venv

# Activate the environment
# On Windows:
.venv\Scripts\activate
# On Mac/Linux:
source .venv/bin/activate

# Install required libraries
pip install undetected-chromedriver beautifulsoup4 pandas webdriver-manager setuptools
```

### 3. Usage
1. Open `Scraper.py`.
2. Update the `TARGET_URL` variable with your desired search filters from Property24.
3. Run the script:
```bash
python Scraper.py
```
4. Once completed, find your data in `johannesburg_rentals_final.csv`.

---

## 🧠 Technical Challenges & Solutions

| Challenge | Solution |
| :--- | :--- |
| **Bot Detection (Cloudflare)** | Switched from standard Selenium to `undetected-chromedriver` to hide the `navigator.webdriver` flag and mimic human behavior. |
| **Dynamic Content** | Implemented explicit wait times to allow JavaScript to render the property tiles before parsing the HTML. |
| **Inconsistent Layouts** | Property24 uses different HTML structures for "Premium" vs "Regular" listings. I implemented a **Landmark-based extractor** that targets semantic `itemprop` attributes rather than fragile CSS classes. |
| **Corporate Firewall** | Encountered `WinError 10054` when downloading drivers. Integrated `webdriver-manager` to handle driver binaries more reliably. |
| **Data Noise** | Found that prices and titles were merged in some tags. Solved this by targeting **hidden meta tags** designed for SEO, ensuring 100% accuracy for numeric values. |

---

## ⚠️ Disclaimer
This project was created for educational purposes. When scraping websites, always:
1. Check the website's `robots.txt` file.
2. Avoid aggressive request rates to prevent overloading the server.
3. Comply with the website's Terms of Service.

---

## 👤 Author
**[Paballo Mofokeng]**
- GitHub: [https://github.com/mofokengpablo0/Pablo_Projects]
- LinkedIn: [www.linkedin.com/in/paballo-mofokeng07]