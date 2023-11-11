"""init migration

Revision ID: 0001
Revises: 
Create Date: 2023-11-11 16:02:41.079073

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('course',
    sa.Column('direction', sa.String(length=32), nullable=False),
    sa.Column('value', sa.Float(precision=6), nullable=True),
    sa.PrimaryKeyConstraint('direction')
    )
    op.create_index(op.f('ix_course_direction'), 'course', ['direction'], unique=False)


def downgrade():
    op.drop_index(op.f('ix_course_direction'), table_name='course')
    op.drop_table('course')
