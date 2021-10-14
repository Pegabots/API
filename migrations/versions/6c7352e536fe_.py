"""empty message

Revision ID: 6c7352e536fe
Revises: cc5846eb4bde
Create Date: 2021-10-14 14:13:23.707627

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c7352e536fe'
down_revision = 'cc5846eb4bde'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('analises', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('analises', sa.Column('updated_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('analises', 'updated_at')
    op.drop_column('analises', 'created_at')
    # ### end Alembic commands ###
