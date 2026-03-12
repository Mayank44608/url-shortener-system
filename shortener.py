import random
import string

url_database = {}

def generate_short_code(length=6):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def shorten_url(long_url):
    short_code = generate_short_code()
    url_database[short_code] = long_url
    return short_code

def get_original_url(short_code):
    return url_database.get(short_code)

# Example
long_url = "https://www.example.com/very-long-url"

short = shorten_url(long_url)

print("Short URL code:", short)
print("Original URL:", get_original_url(short))
