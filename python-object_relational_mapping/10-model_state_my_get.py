#!/usr/bin/python3
"""Find a state by name and display its ID using SQLAlchemy."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    session = Session(engine)

    state = session.query(State).filter(
        State.name == sys.argv[4]
    ).first()

    if state is not None:
        print(state.id)
    else:
        print("Not found")

    session.close()
