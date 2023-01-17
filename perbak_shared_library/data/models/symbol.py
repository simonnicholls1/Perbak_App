from sqlalchemy import Column, String, Boolean
from perbak_shared_library.data.models.base_model import Base


class Symbol(Base):
    __tablename__ = 'symbols'

    symbol = Column(String, primary_key=True)
    active = Column(Boolean)

    def __init__(self, symbol, active):
        self.symbol = symbol
        self.active = active
