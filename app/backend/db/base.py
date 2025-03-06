from sqlalchemy import (
    create_engine
)

from sqlalchemy.orm import (
    DeclarativeBase,
    sessionmaker
)

eng = create_engine('sqlite:///anime_lib.db', echo=True)
Session = sessionmaker(eng)

class Base(DeclarativeBase):
    ...

def create_db():
    Base.metadata.create_all(eng)

def drop_db():
    Base.metadata.drop_all(eng)