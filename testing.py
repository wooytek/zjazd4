import requests

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

    # Access the exchange rate values, e.g. GBP:
    print(1/(data['quotes']['USDEUR']))
    print(data['timestamp'])

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
except (KeyError, TypeError) as e:
    print(f"Error accessing data: {e}.  Check the API response format.")
except Exception as e: # Catch any other potential errors
    print(f"An unexpected error occurred: {e}")