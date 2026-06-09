#!/usr/bin/python3
"""Prints all City objects from the database, joined with their State name."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, db_name
        ),
        pool_pre_ping=True
    )
    with Session(engine) as session:
        rows = session.query(State, City).filter(
            State.id == City.state_id
        ).order_by(City.id).all()
        for state, city in rows:
            print("{}: ({}) {}".format(state.name, city.id, city.name))
