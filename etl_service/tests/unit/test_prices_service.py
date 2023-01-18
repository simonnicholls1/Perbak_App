import pytest
import mock
from etl_service.services.prices_service import eod, PricesService
from collections import namedtuple


def test_fetch_eod_prices_ok(mocker):
    Prices = namedtuple("Prices", "data")
    Price = namedtuple("Price",
                       "symbol date open_ high low close adj_open adj_close adj_high adj_low volume split_factor")
    test_prices = Prices([Price(
        symbol='test_symbol',
        date='2022-01-01',
        open_=132.0,
        high=132.0,
        low=132.0,
        close=132.0,
        adj_open=132.0,
        adj_close=132.0,
        adj_high=132.0,
        adj_low=132.0,
        volume=5000,
        split_factor=1.0
    )])

    with mocker.patch.object(eod, 'sync', return_value=test_prices):
        # Create an instance of MyClass
        price_service = PricesService('key')
        prices = price_service.fetch_eod_prices(['TEST'], '2021-01-01')
        assert len(prices) == len(test_prices.data)
        assert prices[0].symbol == test_prices.data[0].symbol
