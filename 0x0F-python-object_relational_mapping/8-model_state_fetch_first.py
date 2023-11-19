#!/usr/bin/python3
"""prints the first State object from the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    instance = session.query(State).order_by(State.id).first()

    if instance is None:
        print('Nothing')
    else:
        print('{:d}: {:s}'.format(instance.id, instance.name))
