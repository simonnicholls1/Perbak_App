from marketstack.client import Client
from datetime import date, timedelta
from etls.models.price import Price
from marketstack.api.eod import eod

class PricesService:

    def __init__(self, api_key):
        self._api_key = api_key
        protocol = "https"
        self.client = Client(base_url=f"{protocol}://api.marketstack.com/v1")
        self.symbols = "AAPL,AMZN"

    # Function to fetch end-of-day prices from marketstack API
    def fetch_eod_prices(self, symbols):
        end_date = date.today()
        start_date = end_date - timedelta(days=30)
        prices = []
        for symbol in symbols:
            prices_data = eod.sync(
                client=self.client,
                access_key=self._api_key,
                symbols=self.symbols,
                limit=10,
            )

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