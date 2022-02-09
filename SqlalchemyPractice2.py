from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, DateTime, String, desc, create_engine
from sqlalchemy.ext.declarative import declarative_base
import os

engine = create_engine('postgresql+psycopg2://postgres:revulu1@localhost/sqlalchemy_tuts')
engine.connect()
session = Session(bind=engine)

Base = declarative_base()


class Goods(Base):
    __tablename__ = 'GoodsTable'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)
    start_expiration_date = Column(DateTime(), nullable=False)
    end_expiration_date = Column(DateTime(), nullable=False)


Base.metadata.create_all(engine)

goodsfile = '/Users/weainthomiess/Downloads/goods2.info'
new_name = '/Users/weainthomiess/Downloads/goods2.txt'
os.rename(goodsfile, new_name)

with open('/Users/weainthomiess/Downloads/goods2.txt') as goodsfile2:
    strings_of_goods = goodsfile2.readlines()
    list_of_goods = []

    for string_good in strings_of_goods:
        dict_good = dict()
        name, price, amount, start_expiration_date, end_expiration_date, *_ = string_good.split(':')
        dict_good['name'] = name
        dict_good['price'] = price
        dict_good['amount'] = amount
        dict_good['start_expiration_date'] = start_expiration_date
        dict_good['end_expiration_date'] = end_expiration_date

        list_of_goods.append(dict_good)

    for good in list_of_goods:
        good = Goods(
            name=good['name'],
            price=good['price'],
            amount=good['amount'],
            start_expiration_date=good['start_expiration_date'],
            end_expiration_date=good['end_expiration_date']
        )
        session.add(good)
    session.commit()

print(session.query(Goods.name).order_by(desc(Goods.amount)).first())
