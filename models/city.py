#!/usr/bin/python3
"""Defines the City class"""

from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    """the City class inheriting from BaseModel"""
    state_id = ""
    name = ""
