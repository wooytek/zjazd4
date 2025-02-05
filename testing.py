import requests
from datetime import datetime
from fastapi import FastAPI
import uvicorn

# Set API Endpoint and access key
endpoint = 'live'
access_key = '97c2b94caefe3f41f1e216cb59e66baf'

# Construct the URL
url = f'https://api.currencylayer.com/{endpoint}?access_key={access_key}'

# Make the request
try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
    data = response.json()
    quotes={}
    # Access the exchange rate values, e.g. GBP:
    quotes['eurusd'] = 1/(data['quotes']['USDEUR'])
    quotes['usdjpy'] = data['quotes']['USDJPY']
    quote_timestamp = data['timestamp']
    print(1/(data['quotes']['USDEUR']))
    print(data['timestamp'])

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
except (KeyError, TypeError) as e:
    print(f"Error accessing data: {e}.  Check the API response format.")
except Exception as e: # Catch any other potential errors
    print(f"An unexpected error occurred: {e}")

timestamp = datetime.fromtimestamp(quote_timestamp)



app = FastAPI()

@app.get("/currency/{currency_id}")
def get_currency_pair(currency_id: str):
    return {
        "currency": currency_id,
        "quote": round(quotes[currency_id],4),
        "timestamp": timestamp
    }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)