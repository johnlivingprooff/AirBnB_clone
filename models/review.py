#!/usr/bin/python3
"""Defines the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Contains the 'reviews' from users"""
    place_id = ""
    user_id = ""
    text = ""
