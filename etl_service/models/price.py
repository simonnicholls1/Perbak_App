from sqlalchemy import Column, String, Date, Float
from etl_service.models.base_model import Base


class Price(Base):
    __tablename__ = 'prices'

    symbol = Column(String, primary_key=True)
    date = Column(Date, primary_key=True)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    adj_open = Column(Float)
    adj_close = Column(Float)
    adj_high = Column(Float)
    adj_low = Column(Float)
    volume = Column(Float)
    split_factor = Column(Float)

    def __init__(self, symbol, date, open, high, low, close, volume, adj_open, adj_close, adj_high, adj_low,
                 split_factor):
        self.symbol = symbol
        self.date = date
        self.open = open
        self.high = high
        self.low = low
        self.adj_open = adj_open
        self.adj_close = adj_close
        self.adj_high = adj_high
        self.adj_low = adj_low
        self.close = close
        self.volume = volume
        self.split_factor = split_factor

    def __repr__(self):
        return f'<Price(symbol={self.symbol}, date={self.date}, open={self.open}, high={self.high}, low={self.low}, close={self.close}, volume={self.volume})>'
