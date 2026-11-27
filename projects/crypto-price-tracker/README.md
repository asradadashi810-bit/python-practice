# Crypto Price Tracker

Fetches BTC, ETH, DOGE and XRP prices from the API Ninjas API every 5 minutes and appends them to `crypto.csv`.

## Run
```bash
pip install requests
export API_NINJAS_KEY=your_key      # Windows: set API_NINJAS_KEY=your_key
python crypto_tracker.py
```
