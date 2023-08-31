"""Renaming students to scholars

Revision ID: ff81ac32771e
Revises: 791279dd0760
Create Date: 2023-08-31 07:32:10.192489

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff81ac32771e'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students','scholars')


def downgrade() -> None:
    op.rename_table('scholars','students')
