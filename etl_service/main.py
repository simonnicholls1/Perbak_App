from perbak_shared_library.data.database import get_db
import argparse
from etls.prices_etl import PricesETL
# Import imports -> they setup the models!!

#Setup logging
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.propagate = False
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run different ETL scripts')
    parser.add_argument('etl_script', type=str, help='Name of the ETL script to run choices: {prices}')
    parser.add_argument('date', type=str, help='Date to run')
    args = parser.parse_args()
    db = get_db()
    if args.etl_script == 'prices':
        logger.info('Running prices ETL with date: {0}'.format(args.date))
        prices_etl = PricesETL(db)
        prices_etl.run_etl(args.date)
        logger.info('ETL Prices Finished')

