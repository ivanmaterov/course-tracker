"""Init `Course` model.

Revision ID: 0001
Revises:
Create Date: 2023-11-11 22:23:01.769810

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'course',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('direction', sa.String(length=32), nullable=True),
        sa.Column('value', sa.Float(precision=6), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('direction'),
    )
    op.create_index(op.f('ix_course_id'), 'course', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_course_id'), table_name='course')
    op.drop_table('course')
    # ### end Alembic commands ###
