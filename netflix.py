import requests
from bs4 import BeautifulSoup
import re

# URL of the Netflix page
url = input("enter your Netflix url: ")

# Add headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache',
    'GeoIP-Country': 'IN',
    'GeoIP-City': 'Delhi',
}

# Fetch the content of the page with headers
response = requests.get(url, headers=headers)
if response.status_code == 200:
    # Parse the content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Convert soup to a string to search for the image URL
    page_content = str(soup)

    # Use regex to search for the image URL in the content
    image_pattern = re.search(r'"image":"(https://.*?.nflxso.net/.*?.jpg.*?)"', page_content)

    if image_pattern:
        # Extract the image URL
        image_url = image_pattern.group(1)
        print("Image URL:", image_url)
    else:
        print("Image URL not found.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")