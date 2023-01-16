from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#from core.config import settings
from perbak_api.services.secrets_service import SecretsService


secrets_service = SecretsService()
user, password, host, port, name = secrets_service.get_database_credentials()
SQLALCHEMY_DATABASE_URL = f'postgresql://{user}:{password}@{host}:{port}/{name}'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
