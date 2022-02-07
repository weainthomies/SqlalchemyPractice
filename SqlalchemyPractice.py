import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy import Column, Integer, String, PrimaryKeyConstraint, ForeignKeyConstraint, create_engine
from sqlalchemy.ext.declarative import declarative_base

connection = psycopg2.connect(user="postgres", password="revulu1")
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cursor = connection.cursor()
sql_create_database = cursor.execute('create database sqlalchemy_tuts')
cursor.close()
connection.close()

engine = create_engine('postgresql+psycopg2://postgres:revulu1@localhost/sqlalchemy_tuts')
engine.connect()

Base = declarative_base()


class Link(Base):
    """Link table class"""
    __tablename__ = 'link'
    id = Column(Integer, primary_key=True)
    url = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=True)
    rel = Column(String(50), nullable=True)


class Groups(Base):
    """Groups table class"""
    __tablename__ = 'Groups'
    group_id = Column(Integer, nullable=False)
    group_name = Column(String, nullable=True)
    __table_args__ = (PrimaryKeyConstraint('group_id', name='groups_pkey'),)


class Users(Base):
    """Users table class"""
    __tablename__ = 'Users'
    name = Column(String, nullable=True)
    user_id = Column(Integer, nullable=False)
    surname = Column(String, nullable=True)
    group_id = Column(Integer, nullable=True)
    age = Column(Integer, nullable=True)

    __table_args__ = (
        PrimaryKeyConstraint('user_id', name='users_pkey'),
        ForeignKeyConstraint(['group_id'], ['Groups.group_id'], name='groupid'),
    )


Base.metadata.create_all(engine)
