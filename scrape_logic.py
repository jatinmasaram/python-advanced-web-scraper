import requests
from bs4 import BeautifulSoup

def scrape_page(url, headers):
    """
    Scrapes quotes, authors, and tags from a single URL.
    Returns a list of dictionaries with the extracted data,
    or None if an error occurs.
    """
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # This will raise an HTTPError for bad responses
        
        soup = BeautifulSoup(response.text, 'html.parser')
        quote_divs = soup.find_all('div', class_='quote')

        # If no quotes are found, it means we've hit the end of the pages
        if not quote_divs:
            return None

        quotes = []
        for quote_div in quote_divs:
            try:
                quote_text = quote_div.find('span', class_='text').text.strip()
                author_name = quote_div.find('small', class_='author').text.strip()
                
                tags_list = []
                tags_div = quote_div.find('div', class_='tags')
                if tags_div:
                    tags = tags_div.find_all('a', class_='tag')
                    for tag in tags:
                        tags_list.append(tag.text.strip())
                
                quotes.append({
                    'quote': quote_text,
                    'author': author_name,
                    'tags': tags_list
                })
            except AttributeError:
                print(f"Warning: Could not parse a quote on page {url}. Skipping.")
                continue
        
        return quotes
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return None