import requests
from bs4 import BeautifulSoup

def get_product_price(url):
    """Fetches the price of a product from a given URL."""
    try:
        # Simulate a browser request to avoid blocking
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status() # Raise an exception for bad status codes

        soup = BeautifulSoup(response.content, 'html.parser')

        # --- Price extraction logic (this is highly site-specific) ---
        # This is a simplified example. Real-world scrapers need to inspect
        # specific HTML elements for each target website.
        # Common tags/attributes to look for: 'span', 'div', 'class', 'id', 'data-price'
        price_element = soup.find('span', {'class': 'price'})
        if price_element:
            return price_element.get_text(strip=True)
        else:
            # Try another common pattern if the first fails
            price_element_alt = soup.find('div', {'id': 'productPrice'})
            if price_element_alt:
                return price_element_alt.get_text(strip=True)
            else:
                return "Price not found"
        # -------------------------------------------------------------

    except requests.exceptions.RequestException as e:
        return f"Error fetching URL: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

if __name__ == "__main__":
    # Example URLs (replace with actual product pages you want to test)
    # NOTE: These are hypothetical and may not work without specific selectors.
    # You'll need to inspect the HTML of the actual pages.
    product_urls = [
        "https://www.example.com/product/123", # Replace with a real URL
        "https://www.anothersite.com/item/abc", # Replace with a real URL
    ]

    print("--- Price Comparison ---")
    for url in product_urls:
        price = get_product_price(url)
        print(f"URL: {url}\nPrice: {price}\n")

    print("Note: Price extraction logic is highly site-specific and may need adjustments.")
