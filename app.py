from flask import Flask, request, redirect
import random
import string

app = Flask(__name__)

url_database = {}

def generate_short_code(length=6):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form['url']
    short_code = generate_short_code()
    url_database[short_code] = long_url
    return {"short_url": f"http://localhost:5000/{short_code}"}

@app.route('/<short_code>')
def redirect_url(short_code):
    long_url = url_database.get(short_code)
    if long_url:
        return redirect(long_url)
    return "URL not found"

if __name__ == "__main__":
    app.run(debug=True)
