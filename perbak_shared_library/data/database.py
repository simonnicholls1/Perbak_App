from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#from core.config import settings
from perbak_shared_library.services.secrets_service import SecretsService

def get_db_sql_url():
    user, password, host, port, name = secrets_service.get_database_credentials()
    url = f'postgresql+psycopg2://{user}@{host}:{password}@{host}:{port}/{name}'
    return url


def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()

secrets_service = SecretsService()
url = get_db_sql_url()
engine = create_engine(url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


