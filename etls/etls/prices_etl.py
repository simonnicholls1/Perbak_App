from etls.services.prices_service import PricesService
import os

class PricesETL():

    def __init__(self, db_session):
        api_key = os.environ.get('MARKETSTACK_API_KEY')
        self.prices_service = PricesService(api_key)
        self.db_session = db_session

    def run_etl(self):
        # Fetch end-of-day prices

        symbols = ['AAPL', 'GOOG', 'AMZN']
        prices = self.prices_service.fetch_eod_prices(symbols)

        self.db_session.add_all(prices)
        self.db_session.commit()
        self.db_session.close()