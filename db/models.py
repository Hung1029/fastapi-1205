from .database import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey


class DbArticle(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    sku = Column(String)
    description = Column(String)
    description_long = Column(String)
    owner_id = Column(Integer, ForeignKey('user.id'))
    owner = relationship('DbUser', back_populates ='created_articles')
    comment_article = relationship('DbComment', back_populates ='article_comments')
    like_article = relationship('DbLike', back_populates ='article_likes')


class DbUser(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    is_admin = Column(Boolean)
    created_articles = relationship('DbArticle', back_populates='owner')
    comment_user = relationship('DbComment', back_populates ='user_comments')
    like_user = relationship('DbLike', back_populates='user_likes')


class DbComment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    content = Column(String)
    article_id = Column(Integer, ForeignKey('article.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    user_comments = relationship('DbUser',back_populates='comment_user')
    article_comments = relationship('DbArticle', back_populates ='comment_article')

class DbLike(Base):
    __tablename__ = 'like'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    article_id = Column(Integer, ForeignKey('article.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    article_likes= relationship('DbArticle', back_populates ='like_article')
    user_likes = relationship('DbUser', back_populates='like_user')


