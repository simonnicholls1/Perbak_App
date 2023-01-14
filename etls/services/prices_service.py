from marketstack import MarketStack
from datetime import date, timedelta
from etls.models.price import Price

class PricesService:

    def __init__(self, api_key):
        self._api_key = api_key

    # Function to fetch end-of-day prices from marketstack API
    def fetch_eod_prices(self, symbols):
        marketstack = MarketStack(self._api_key)
        end_date = date.today()
        start_date = end_date - timedelta(days=30)
        prices = []
        for symbol in symbols:
            prices_data = marketstack.eod(symbol, start_date.isoformat(), end_date.isoformat())
            for data in prices_data['data']:
                prices.append(Price(
                    symbol=symbol,
                    date=data['date'],
                    open=data['open'],
                    high=data['high'],
                    low=data['low'],
                    close=data['close'],
                    volume=data['volume']
                ))
        return prices