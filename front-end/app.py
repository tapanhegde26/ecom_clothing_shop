from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # Fetch product data from the backend
    products = requests.get('http://backend:5000/products').json()
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

