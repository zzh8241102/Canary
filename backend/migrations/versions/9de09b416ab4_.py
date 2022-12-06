"""empty message

Revision ID: 9de09b416ab4
Revises: 
Create Date: 2022-12-06 15:55:43.488400

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9de09b416ab4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('User',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(length=20), nullable=False),
    sa.Column('user_password', sa.String(length=200), nullable=False),
    sa.Column('user_email', sa.String(length=50), nullable=True),
    sa.Column('user_phone', sa.String(length=20), nullable=True),
    sa.Column('user_reg_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('Article',
    sa.Column('article_id', sa.Integer(), nullable=False),
    sa.Column('article_title', sa.String(length=100), nullable=False),
    sa.Column('article_content', sa.Text(), nullable=False),
    sa.Column('article_author', sa.Integer(), nullable=True),
    sa.Column('published_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['article_author'], ['User.user_id'], ),
    sa.PrimaryKeyConstraint('article_id')
    )
    op.create_table('UserTags',
    sa.Column('user_tag_id', sa.Integer(), nullable=False),
    sa.Column('user_tag_name', sa.String(length=20), nullable=False),
    sa.Column('user_tag_owner', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_tag_owner'], ['User.user_id'], ),
    sa.PrimaryKeyConstraint('user_tag_id')
    )
    op.create_table('Comments',
    sa.Column('comment_id', sa.Integer(), nullable=False),
    sa.Column('comment_content', sa.Text(), nullable=False),
    sa.Column('comment_author', sa.Integer(), nullable=True),
    sa.Column('comment_article', sa.Integer(), nullable=True),
    sa.Column('comment_time', sa.DateTime(), nullable=True),
    sa.Column('comment_likes', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['comment_article'], ['Article.article_id'], ),
    sa.ForeignKeyConstraint(['comment_author'], ['User.user_id'], ),
    sa.PrimaryKeyConstraint('comment_id')
    )
    op.create_table('Likes',
    sa.Column('like_id', sa.Integer(), nullable=False),
    sa.Column('like_corr_article', sa.Integer(), nullable=True),
    sa.Column('like_corr_user', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['like_corr_article'], ['Article.article_id'], ),
    sa.ForeignKeyConstraint(['like_corr_user'], ['User.user_id'], ),
    sa.PrimaryKeyConstraint('like_id')
    )
    op.create_table('Tags',
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.Column('tag_name', sa.String(length=20), nullable=False),
    sa.Column('tag_corr_article', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['tag_corr_article'], ['Article.article_id'], ),
    sa.PrimaryKeyConstraint('tag_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Tags')
    op.drop_table('Likes')
    op.drop_table('Comments')
    op.drop_table('UserTags')
    op.drop_table('Article')
    op.drop_table('User')
    # ### end Alembic commands ###
