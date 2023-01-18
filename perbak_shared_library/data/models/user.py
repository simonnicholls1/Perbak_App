from sqlalchemy import Column, String, Integer
from perbak_shared_library.data.models.base_model import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    #Plain text password change this!!
    password = Column(String(15), nullable=False)