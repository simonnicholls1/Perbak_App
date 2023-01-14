from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists

def create_db(db_url):
    if not database_exists(db_url):
        create_database(db_url)
        print(f'Successfully created database at {db_url}')
    else:
        print(f'Database at {db_url} already exists')

if __name__ == '__main__':
    db_url = 'postgresql://username:password@host:port/dbname'
    create_db(db_url)
