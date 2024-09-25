import urllib.request
import urllib.error
import gzip

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

    # Set up the request with headers
    req = urllib.request.Request(url, headers=headers)

    try:
        # Fetch the content of the page
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                # Check if the response is compressed
                if response.headers.get('Content-Encoding') == 'gzip':
                    # Decompress the content
                    page_content = gzip.decompress(response.read()).decode('utf-8')
                else:
                    # If not compressed, just read and decode as usual
                    page_content = response.read().decode('utf-8')

                # Look for the "og:image" meta tag manually in the HTML
                og_image_tag = 'property="og:image" content="'
                start_idx = page_content.find(og_image_tag)
                
                if start_idx != -1:
                    start_idx += len(og_image_tag)
                    end_idx = page_content.find('"', start_idx)
                    poster_url = page_content[start_idx:end_idx]
                    return poster_url
                else:
                    return "Poster image not found on the page."
            else:
                return f"Failed to retrieve the page. Status code: {response.status}"
    
    except urllib.error.URLError as e:
        return f"Failed to retrieve the page. Error: {e}"
