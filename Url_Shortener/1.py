import hashlib

class URLShortener:
    def __init__(self):
        self.url_mapping = {}
    
    def shorten_url(self, long_url):
        # Generate a unique hash for the long URL
        hash_object = hashlib.md5(long_url.encode())
        hash_hex = hash_object.hexdigest()
        
        # Take the first 8 characters of the hash as the short URL
        short_url = hash_hex[:8]
        
        # Store the mapping of short URL to long URL
        self.url_mapping[short_url] = long_url
        
        return short_url
    
    def expand_url(self, short_url):
        # Retrieve the long URL from the mapping
        long_url = self.url_mapping.get(short_url)
        return long_url

# Example usage
if __name__ == "__main__":
    shortener = URLShortener()
    long_url = "https://www.example.com/some/very/long/url/to/be/shortened"
    
    short_url = shortener.shorten_url(long_url)
    print(f"Short URL: {short_url}")
    
    original_url = shortener.expand_url(short_url)
    print(f"Original URL: {original_url}")