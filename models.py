# models.py
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class AuthorDB(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    bio = Column(String, index=True)

    # Relationship to the BookDB model
    books = relationship("BookDB", back_populates="author")

class BookDB(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    summary = Column(String, index=True)
    genres = Column(String, index=True)
    author_id = Column(Integer, ForeignKey('authors.id'))

    # Relationship to the AuthorDB model
    author = relationship("AuthorDB", back_populates="books")
