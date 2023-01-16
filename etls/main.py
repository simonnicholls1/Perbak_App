import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Connect to the database
DATABASE_URL = os.environ.get('DATABASE_URL')
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)





if __name__ == "__main__":
    etl()
