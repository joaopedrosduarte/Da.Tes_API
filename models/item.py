from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, BigInteger
from config.db import meta

item = Table(
    'item', meta,
    Column('id', BigInteger, primary_key=True),
    Column('name', String(30)),
    Column('price', BigInteger),
)