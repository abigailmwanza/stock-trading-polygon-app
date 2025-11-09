import requests
import os
import csv
from dotenv import load_dotenv

load_dotenv()

POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")
LIMIT = 1000

# Base URL for tickers
url = f"https://api.polygon.io/v3/reference/tickers?market=stocks&active=true&order=asc&limit={LIMIT}&sort=ticker&apiKey={POLYGON_API_KEY}"
response = requests.get(url)

data = response.json()
print('Initial API response keys:', list(data.keys()))  # quick debug

tickers = []

# Only loop if 'results' key exists
if 'results' in data:
    for ticker in data['results']:
        tickers.append(ticker)
else:
    print("No 'results' key found — check your API response or key validity.")

# Handle pagination if available (Polygon may return "next_url")
while data.get('next_url'):
    next_url = data['next_url']
    print('Requesting next page:', next_url)
    # next_url may already include query params; ensure apiKey is present
    if 'apiKey=' not in next_url:
        next_url = next_url + ('' if next_url.endswith('?') else '&') + f'apiKey={POLYGON_API_KEY}'
    response = requests.get(next_url)
    data = response.json()
    if 'results' in data:
        for ticker in data['results']:
            tickers.append(ticker)
    else:
        break

# Example schema (taken from existing example_ticker)
example_ticker = {
    'ticker': 'BATRA',
    'name': 'Atlanta Braves Holdings, Inc.  Series A Common Stock',
    'market': 'stocks',
    'locale': 'us',
    'primary_exchange': 'XNAS',
    'type': 'CS',
    'active': True,
    'currency_name': 'usd',
    'cik': '0001958140',
    'composite_figi': 'BBG01HCDRG86',
    'share_class_figi': 'BBG01HCDRG95',
    'last_updated_utc': '2025-11-08T07:06:06.688585738Z'
}

# Use the keys of example_ticker as the CSV header, preserving order
csv_headers = list(example_ticker.keys())

output_file = 'tickers.csv'

def safe_get(d, key):
    """Return d[key] if present, else empty string; convert booleans to lowercase strings for CSV."""
    v = d.get(key, '') if isinstance(d, dict) else ''
    if isinstance(v, bool):
        return str(v)
    return v

print('Writing', len(tickers), 'tickers to', output_file)
with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=csv_headers)
    writer.writeheader()
    for t in tickers:
        # Build a row that only has the keys in csv_headers
        row = {k: safe_get(t, k) for k in csv_headers}
        writer.writerow(row)

print('Wrote', output_file)


