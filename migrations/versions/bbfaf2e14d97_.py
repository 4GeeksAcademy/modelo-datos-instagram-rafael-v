"""empty message

Revision ID: bbfaf2e14d97
Revises: a5cffa318ac2
Create Date: 2025-06-05 23:52:03.351642

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bbfaf2e14d97'
down_revision = 'a5cffa318ac2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('follower',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('photo', sa.String(length=100), nullable=False),
    sa.Column('comments', sa.String(length=250), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('photo', sa.String(length=100), nullable=False),
    sa.Column('comments', sa.String(length=250), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('answers', sa.String(length=250), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('media',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('photo', sa.String(length=100), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('location', sa.String(length=100), nullable=False))
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=120),
               type_=sa.String(length=50),
               existing_nullable=False)
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=250),
               existing_nullable=False)
        batch_op.drop_constraint('user_email_key', type_='unique')
        batch_op.drop_column('is_active')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False))
        batch_op.create_unique_constraint('user_email_key', ['email'])
        batch_op.alter_column('password',
               existing_type=sa.String(length=250),
               type_=sa.VARCHAR(length=80),
               existing_nullable=False)
        batch_op.alter_column('email',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=120),
               existing_nullable=False)
        batch_op.drop_column('location')

    op.drop_table('media')
    op.drop_table('comment')
    op.drop_table('post')
    op.drop_table('follower')
    # ### end Alembic commands ###
