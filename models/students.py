from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String
from config.db import meta,engine

students = Table(
    'students',meta,
    Column('id',Integer,primary_key=True),
    Column('name',String(2205)),
    Column('email',String(225)),
    Column('age',Integer),
    Column('country',String(225))
)

meta.create_all(bind=engine)