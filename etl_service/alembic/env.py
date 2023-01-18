# alembic/env.py
from __future__ import with_statement
import sys
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
APP_DIR = os.path.join(BASE_DIR, '../')
sys.path.append(APP_DIR)
from alembic import context
from sqlalchemy import create_engine
from perbak_shared_library.data.database import get_db_sql_url

# add model's MetaData object here, need to import models to get the metadata
from perbak_shared_library.data.models.price import Price
from perbak_shared_library.data.models.user import User
from perbak_shared_library.data.models.symbol import Symbol
from perbak_shared_library.data.models.base_model import Base
target_metadata = Base.metadata
if len(target_metadata.tables) == 0:
    raise ValueError('Please make sure you have imported the model tables to add to base metadata as this could really mess with alembic!!')
url = get_db_sql_url()
# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.

def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = create_engine(url)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
