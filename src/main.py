from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from scraper.scraper import Scraper

with open("queries.txt", "r") as file:
    SEARCH_QUERIES = [line.strip() for line in file]

def main():
    # Initialize the Selenium WebDriver
    driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and in PATH
    try:
        # Set the selectedCurrency key in local storage
        driver.get("https://app.getcollectr.com")  # Open the website to access local storage
        currency_data = {
            "currency": "CAD",
            "rate": "1.396740224324435",
            "symbol": "$",
            "icon": "https://public.getcollectr.com/public-assets/currency-symbols/CAD.svg?optimizer=image&format=webp&width=800&quality=85&strip=metadata",
            "name": "Canadian Dollar",
            "code": "CAD"
        }
        driver.execute_script(f"window.localStorage.setItem('selectedCurrency', '{str(currency_data).replace('\'', '\"')}');")
        print("Currency set to CAD in local storage.")

        # Check if there are queries in the file
        if len(SEARCH_QUERIES) > 8:  # Ensure there is a ninth query
            ninth_query = SEARCH_QUERIES[8]  # Get the ninth query (EB01)
            url = f"https://app.getcollectr.com/?query={ninth_query}"  # Construct the URL
            print(f"Navigating to URL: {url}")

            # Navigate to the constructed URL
            driver.get(url)

            # Create an instance of the Scraper class
            scraper = Scraper(driver)

            # Perform the search and scrape for the ninth query
            print(f"Scraping data for query: {ninth_query}")
            scraper.search_and_scrape(ninth_query)
        else:
            print("No ninth query found in queries.txt")

    finally:
        # Close the WebDriver
        driver.quit()

if __name__ == "__main__":
    main()