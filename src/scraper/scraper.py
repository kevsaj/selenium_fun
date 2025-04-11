import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Scraper:
    def __init__(self, driver):
        self.driver = driver

    def search_and_scrape(self, search_query):
        # Navigate to the URL with the query
        url = f"https://app.getcollectr.com/?query={search_query}"
        self.driver.get(url)

        # Wait for the page to fully load
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "body"))  # Wait for the body tag to load
        )

        # Scroll to load all lazy-loaded cards
        self.scroll_to_load_all()

        # Wait for cards to load
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.pb-5 > div.flex.flex-col.h-full"))
        )

        # Scrape card details
        cards = self.driver.find_elements(By.CSS_SELECTOR, "div.pb-5 > div.flex.flex-col.h-full")
        card_data = []
        for card in cards:
            try:
                # Extract card details using specific selectors
                name = card.find_element(By.CSS_SELECTOR, "h3").text
                category = card.find_element(By.CSS_SELECTOR, "p.underline").text
                rarity = card.find_elements(By.CSS_SELECTOR, "div.flex.flex-col p")[1].text
                sku_id = card.find_elements(By.CSS_SELECTOR, "div.flex.flex-col p")[2].text
                price = card.find_element(By.CSS_SELECTOR, "h2").text
                card_data.append([name, category, rarity, sku_id, price])
            except Exception as e:
                print(f"Error scraping card: {e}")

        # Save to CSV
        self.save_to_csv(search_query, card_data)

    def scroll_to_load_all(self):
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        scroll_attempts = 0  # Track the number of scroll attempts without new content
        previous_card_count = 0  # Track the number of cards loaded

        while True:
            # Scroll to the bottom of the page
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(7)  # Wait for 7 seconds after each scroll

            # Check the number of cards loaded
            cards = self.driver.find_elements(By.CSS_SELECTOR, "div.pb-5 > div.flex.flex-col.h-full")
            current_card_count = len(cards)
            print(f"Cards loaded: {current_card_count}")

            # If no new cards are loaded, increment the scroll attempts
            if current_card_count == previous_card_count:
                scroll_attempts += 1
                if scroll_attempts >= 10:  # Stop after 10 attempts with no new cards
                    print("Reached the bottom of the page. All cards should be loaded.")
                    break
            else:
                scroll_attempts = 0  # Reset attempts if new cards are loaded

            previous_card_count = current_card_count
            last_height = self.driver.execute_script("return document.body.scrollHeight")

    def save_to_csv(self, search_query, card_data):
        filename = f"{search_query}_cards.csv"
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Category", "Rarity", "SKU ID", "Price"])
            writer.writerows(card_data)
        print(f"Data saved to {filename}")