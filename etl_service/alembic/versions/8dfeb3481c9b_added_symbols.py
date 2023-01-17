"""added-symbols

Revision ID: 8dfeb3481c9b
Revises: 220de74a4df0
Create Date: 2023-01-16 16:24:08.099025

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8dfeb3481c9b'
down_revision = '220de74a4df0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('symbols',
    sa.Column('symbol', sa.String(), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('symbol')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('symbols')
    # ### end Alembic commands ###
