"""empty message

Revision ID: c384ba7f77e0
Revises: 
Create Date: 2020-11-10 19:18:04.770469

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c384ba7f77e0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('isbn', sa.BigInteger(), nullable=False),
    sa.Column('vendible', sa.Boolean(), nullable=False),
    sa.Column('stock', sa.Integer(), nullable=False),
    sa.Column('precio', sa.Float(), nullable=False),
    sa.Column('titulo', sa.String(), nullable=False),
    sa.Column('autor', sa.String(), nullable=True),
    sa.Column('editorial', sa.String(), nullable=True),
    sa.Column('sinopsis', sa.String(), nullable=True),
    sa.Column('url_imagen', sa.String(), nullable=True),
    sa.Column('fecha_de_publicacion', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('isbn')
    )
    op.create_table('transactions',
    sa.Column('id_transaction', sa.Integer(), nullable=False),
    sa.Column('isbn', sa.BigInteger(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id_transaction')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('role', sa.Enum('User', 'Admin', name='roles_types'), nullable=False),
    sa.Column('state', sa.Boolean(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('library',
    sa.Column('isbn', sa.BigInteger(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('library_type', sa.Enum('Bought', 'WishList', name='library_types'), nullable=False),
    sa.Column('state', sa.Enum('Pending', 'Reading', 'Finished', 'Dropped', name='state_types'), nullable=False),
    sa.Column('visible', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['isbn'], ['books.isbn'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('isbn', 'user_id', 'library_type')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('library')
    op.drop_table('users')
    op.drop_table('transactions')
    op.drop_table('books')
    # ### end Alembic commands ###