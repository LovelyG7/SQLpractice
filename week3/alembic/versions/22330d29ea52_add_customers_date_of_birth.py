"""add customers date_of_birth

Revision ID: 22330d29ea52
Revises: 5ff7d1efb36b
Create Date: 2022-05-10 16:44:52.561570

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22330d29ea52'
down_revision = '5ff7d1efb36b'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE customers
        ADD COLUMN date_of_birth TIMESTAMP;
        """
    ) 


def downgrade():
    op.execute(
        """
        ALTER TABLE customers
        DROP COLUMN date_of_birth;
        """
    )
