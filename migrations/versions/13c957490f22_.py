"""empty message

Revision ID: 13c957490f22
Revises: d5e8c24d715d
Create Date: 2024-01-10 11:45:18.153777

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13c957490f22'
down_revision = 'd5e8c24d715d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('analises', sa.Column('handle', sa.String(length=80), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('analises', 'handle')
    # ### end Alembic commands ###