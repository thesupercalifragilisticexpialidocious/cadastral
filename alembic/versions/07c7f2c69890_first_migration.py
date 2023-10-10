"""First migration

Revision ID: 07c7f2c69890
Revises: 
Create Date: 2023-10-10 00:21:51.090801

"""
from alembic import op
import sqlalchemy as sa


revision = '07c7f2c69890'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('inquiry',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.Column('number', sa.String(length=32), nullable=True),
    sa.Column('result', sa.String(length=10), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.CheckConstraint('-90 <= latitude AND latitude <= 90 AND -180 <= longitude AND longitude <= 180'),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('inquiry')
