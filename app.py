from flask import Flask, render_template, request, redirect, url_for
import API_request

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def generate_url(params):
    url = f'https://vmsn-app-planner3test.azurewebsites.net/status/market/bid-result?ForDate={params['ForDate']}&Market={params['Market']}&CustomerId={params['CustomerId']}&Country={params['Country']}'
    return url

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch', methods=['POST'])
def fetch():
    apikey = request.form['apikey']
    for_date = request.form['forDate']
    market = request.form['market']
    customer_id = request.form['customerId']
    country = request.form['country']

    headers = {
        'accept': 'text/plain',
        'ApiKey': apikey
    }
    params = {
        'ForDate': for_date,
        'Market': market,
        'CustomerId': customer_id,
        'Country': country
    }

    url = generate_url(params)
    
    API_request.fetch_and_store_json(url, headers, params)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
