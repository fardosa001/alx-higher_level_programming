#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(City, State).join(State)

    for ct, st in query.all():
        print("{}: ({:d}) {}".format(st.name, ct.id, ct.name))

    session.commit()
    session.close()
