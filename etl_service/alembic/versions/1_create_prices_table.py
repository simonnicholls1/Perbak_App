# alembic/versions/1_create_prices_table.py

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '1'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'prices',
        sa.Column('symbol', sa.String(), primary_key=True),
        sa.Column('date', sa.Date(), primary_key=True),
        sa.Column('open', sa.Float(), nullable=False),
        sa.Column('high', sa.Float(), nullable=False),
        sa.Column('low', sa.Float(), nullable=False),
        sa.Column('close', sa.Float(), nullable=False),
        sa.Column('volume', sa.Float(), nullable=False)
    )

def downgrade():
    op.drop_table('prices')
