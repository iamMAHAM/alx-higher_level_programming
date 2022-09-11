#!/usr/bin/python3
"""
lists all State objects from a database
"""

from sqlalchemy import create_engine
from sqlalchemy import sessionmaker
from sys import argv
from model_state import State, Base

if __name__ == '__main__':
    engine = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).order_by(State.id):
        print(f"{state.id}: {state.id}")
    session.close()