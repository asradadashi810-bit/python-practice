"""Save crypto prices to a CSV file every 5 minutes (API Ninjas).

Needs: pip install requests
Set your key first (never write the key inside the code):
    Windows (cmd):    set API_NINJAS_KEY=your_key
    Linux / macOS:    export API_NINJAS_KEY=your_key
"""

import csv
import os
import time

import requests

API_KEY = os.environ.get("API_NINJAS_KEY")
if not API_KEY:
    raise SystemExit("Please set the API_NINJAS_KEY environment variable first.")

SYMBOLS = ["BTCUSDT", "ETHUSDT", "DOGEUSDT", "XRPUSDT"]
FILE_NAME = "crypto.csv"
INTERVAL = 300  # seconds

with open(FILE_NAME, "w", newline="") as f:
    csv.writer(f).writerow(SYMBOLS)

while True:
    prices = []

    for symbol in SYMBOLS:
        url = f"https://api.api-ninjas.com/v1/cryptoprice?symbol={symbol}"
        response = requests.get(url, headers={"X-Api-Key": API_KEY}, timeout=10)
        info = response.json()
        print(info["symbol"], info["price"])
        prices.append(info["price"])

    with open(FILE_NAME, "a", newline="") as f:
        csv.writer(f).writerow(prices)

    time.sleep(INTERVAL)
