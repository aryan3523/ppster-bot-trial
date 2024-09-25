import requests
import re

def scrape_amazon_prime_covershot(url):
    # Send a GET request to the URL
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve page: {response.status_code}")
        return None

    # Search for the first occurrence of 'covershot' in the page content
    match = re.search(r'\"covershot\":\"(https://m\.media-amazon\.com/images/[^\"]+)\"', response.text)

    if match:
        # Extract and return the covershot URL
        covershot_url = match.group(1)
        return covershot_url
    else:
        print("Covershot URL not found.")
        return None

# Example usage
if __name__ == '__main__':
    url = input("Enter the Amazon Prime Video URL: ")
    covershot_url = scrape_amazon_prime_covershot(url)
    
    if covershot_url:
        print("Covershot URL:")
        print(covershot_url)
    else:
        print("Covershot not found.")