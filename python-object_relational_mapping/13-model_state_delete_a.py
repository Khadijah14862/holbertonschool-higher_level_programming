#!/usr/bin/python3
"""Delete states containing the letter a using SQLAlchemy."""

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

    session.query(State).filter(
        State.name.like("%a%")
    ).delete(synchronize_session=False)

    session.commit()

    session.close()
