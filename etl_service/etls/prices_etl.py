from etl_service.services.prices_service import PricesService
from sqlalchemy.dialects.postgresql import insert
from perbak_shared_library.data.models.price import Price
from perbak_shared_library.data.models.symbol import Symbol
from perbak_shared_library.services.secrets_service import SecretsService
from sqlalchemy import and_
import logging

logger = logging.getLogger(__name__)

class PricesETL():

    def __init__(self, db_session):
        secret_service = SecretsService()
        api_key = secret_service.get_marketstack_api_details()
        self.prices_service = PricesService(api_key)
        self.db_session = db_session

    def run_etl(self, date):
        # Fetch end-of-day prices

        #Grab symbols that are active
        symbols = self.db_session.query(Symbol.symbol).filter(and_(Symbol.active == True)).all()
        #Funny return value that returns tuple so just get the names
        symbols = [symbol[0] for symbol in symbols]
        #Api needs it in a string list
        symbols_string = ','.join(symbols)
        #Grab the prices
        prices = self.prices_service.fetch_eod_prices(symbols_string, date)

        try:
            # Need in dict format which is a bit of a pain but this is for upsert
            prices_dicts = []
            for price in prices:
                dict = {k: v for k, v in vars(price).items() if not k.startswith('_')}
                prices_dicts.append(dict)
            if len(prices_dicts) ==0:
                logger.warning('No prices to insert!!')
                self.db_session.close()
                return
            #Insert into DB with upsert (i.e. only add new values)
            logger.info('Inserting {0} rows into the prices table'.format(len(prices_dicts)))
            self.db_session.execute(insert(Price)
                     .values(prices_dicts)
                     .on_conflict_do_nothing())
            self.db_session.commit()
        except:
            logger.error(f"Error! Rolling back")
            self.db_session.rollback()
            raise
        finally:
            self.db_session.close()
