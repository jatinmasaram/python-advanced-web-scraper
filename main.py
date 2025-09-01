import time
from random import uniform
from scrape_logic import scrape_page
from data_processor import save_to_csv

# Base URL for the website
BASE_URL = "http://quotes.toscrape.com/page/"
# User-Agent header to mimic a real browser
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

def main():
    """
    Main function to orchestrate the scraping process.
    """
    all_quotes = []
    page_number = 1
    
    print("Starting to scrape quotes from quotes.toscrape.com...")

    while True:
        url = f"{BASE_URL}{page_number}/"
        print(f"Scraping page: {page_number} ({url})")
        
        quotes_on_page = scrape_page(url, HEADERS)
        
        if quotes_on_page is None:
            # The scrape_page function returns None if it fails or finds no quotes
            print("No more quotes found or an error occurred. End of scraping.")
            break
        
        all_quotes.extend(quotes_on_page)
        
        # Add a random delay to be respectful to the server
        delay = uniform(1, 3)
        print(f"Pausing for {delay:.2f} seconds...")
        time.sleep(delay)
        
        page_number += 1
    
    print(f"\nScraping finished. Total quotes collected: {len(all_quotes)}")
    
    # Save all the collected data to a single CSV file
    save_to_csv(all_quotes, 'all_quotes_modular.csv')

if __name__ == "__main__":
    main()