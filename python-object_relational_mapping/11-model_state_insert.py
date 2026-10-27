#!/usr/bin/python3
"""Insert a new state into the MySQL database using SQLAlchemy."""

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

    new_state = State(name="Louisiana")

    session.add(new_state)
    session.commit()

    print(new_state.id)

    session.close()
