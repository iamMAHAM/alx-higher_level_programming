#!/usr/bin/python3
"""
list all State objects that contain the letter a from a database
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/\
                            {argv[3]}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    s = '%a%'
    states = session.query(State).filter(State.name.like(s)).order_by(State.id)
    for state in states:
        print(f"{state.id}: {state.name}")
    session.close()
