#!/usr/bin/python3
""" python file that contains the class definition of a State"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class that inherits from base"""
    __tablename__ = 'state'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
