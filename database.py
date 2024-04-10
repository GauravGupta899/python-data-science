from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import base
from sqlalchemy import Column, Integer, String, ForeignKey,DateTime

from datetime import datetime # small letters

Base =declarative_base()
# object relationn mapping
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True)
    name = Column(String(50))
    email = Column(String(50), unique =True)
    password = Column(String(64))
    created_at = Column(DateTime, default=datetime.now)

class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer,primary_key=True)
    user_id = Column(Integer,ForeignKey('users.id'))
    message = Column(String(255))
    created_at = Column(DateTime, default=datetime.now)

class Imageupload(Base):
    __tablename__ = 'image_upload'
    id = Column(Integer,primary_key=True)
    __path__= Column(String(255))
    user_id =Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.now)

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer,primary_key=True)
    title =Column(String(255))
    content=Column(String)
    user_id =Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.now) 


#utility functions

def get_db():
   engine = create_engine('sqlite:///example.db')  
   return sessionmaker(bind= engine)()  

def save_to_db(object):
    db = get_db()   # open databse
    db.add(object)   #insert object
    db.commit()     # save change
    db.close()      # close database


#create database
if __name__ == "__main__":
    engine = create_engine('sqlite:///example.db')
    Base.metadata.create_all(engine)