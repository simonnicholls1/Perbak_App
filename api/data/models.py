from sqlalchemy import Column, String, Date,Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Price(Base):
    __tablename__ = 'prices'

    symbol = Column(String, primary_key=True)
    date = Column(Date, primary_key=True)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Float)

    def __init__(self, symbol, date, open, high, low, close, volume):
        self.symbol = symbol
        self.date = date
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

    def __repr__(self):
        return f'<Price(symbol={self.symbol}, date={self.date}, open={self.open}, high={self.high}, low={self.low}, close={self.close}, volume={self.volume})>'
