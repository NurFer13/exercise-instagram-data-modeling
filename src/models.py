import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250),unique=True, nullable=False)
    firstname = Column(String(200),unique=True,nullable=False)
    lastname = Column(String(250),nullable=False)
    email = Column(String(200),nullable=False)
    follower = relationship('Follower',back_populates='user')


class Follower(Base):
    __tablename__ = 'follower'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('person.id'))
    user = relationship('User',back_populates='follower')

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(500),nullable=True)
    author_id = Column(Integer,primary_key=True)
    post_id = Column(Integer,primary_key=True)
    

class Post(Base):
    __tablename__ = 'post'  
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('person.id'))
    media = relationship('Media',back_populates='post')



class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(enumerate(),nullable=False)
    url = Column(String(300),unique=True,nullable=False)
    post_id = Column(Integer,ForeignKey('post_id'))
    post = relationship('Post',back_populates='media')
    

    


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
