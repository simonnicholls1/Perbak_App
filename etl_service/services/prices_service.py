from marketstack.client import Client
from perbak_shared_library.data.models.price import Price
from marketstack.api.eod import eod
import logging

logger = logging.getLogger(__name__)

class PricesService:

    def __init__(self, api_key):
        self._api_key = api_key
        protocol = "http"
        self.client = Client(base_url=f"{protocol}://api.marketstack.com/v1")

    # Function to fetch end-of-day prices from marketstack API
    def fetch_eod_prices(self, symbols, start_date, end_date=None):
        logger.info('Getting end of day prices for symbols {0}'.format(symbols))
        prices = []

        prices_data = eod.sync(
            client=self.client,
            access_key=self._api_key,
            symbols=symbols,
            date_from=start_date,
            date_to=end_date
        )

        for data in prices_data.data:
            prices.append(Price(
                symbol=data.symbol,
                date=data.date,
                open=data.open_,
                high=data.high,
                low=data.low,
                close=data.close,
                adj_open=data.adj_open,
                adj_close=data.adj_close,
                adj_high=data.adj_high,
                adj_low=data.adj_low,
                volume=data.volume,
                split_factor=data.split_factor
            ))
        logger.info('Found prices!')
        return prices