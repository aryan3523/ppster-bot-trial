import requests
from bs4 import BeautifulSoup

def bms_poster(url):
    # Add headers to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36',
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

        # Find the meta tag with property "og:image"
        meta_tag = soup.find('meta', property='og:image')

        # Extract the content attribute
        if meta_tag and 'content' in meta_tag.attrs:
            poster_url = meta_tag['content']
            return poster_url
        else:
            return "Poster image not found on the page."
    else:
        return f"Failed to retrieve the page. Status code: {response.status_code}"
