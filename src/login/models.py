from .database import Base;
from sqlalchemy import Column, String, Integer

class User(Base):
    _tablename_="ourusers"

    id=Column(Integer,primary_key=True,index=True)
    username=Column(String,unique=True, index=True)
    password=Column(String)