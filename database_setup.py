#!/usr/bin/env python3
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
# declarative_base() is a factory function that constructs a base class for 
# declarative class definitions so that we can construct other classes using
# Base variable.
Base = declarative_base()

#Every class corresponds to the table in the database.
class TwitterData(Base):
    __tablename__ = 'twitterdata'
    #Creating the columns for our table with respective datatypes.
    Text = Column(String(20000))
    Hashtags = Column(String(2500))
    FavCount = Column(String(100))
    Language = Column(String(100))
    Place = Column(String(1000))
    UserLocation = Column(String(1000))
    RetweetCount = Column(String(100))
    Date = Column(String(1000))
    Sentiment = Column(String(3000))
    Polarity = Column(String(200))
    id = Column(Integer, primary_key=True)

    # Function Declaration for Flask API.
    @property
    # serialize property will be used to call the JSON properties
    # as defined below.
    def serialize(self):
        return {
               # Declaring the way how the JSON will be represented.
              'Hashtags' : self.Hashtags,
              'FavCount' : self.FavCount,
              'Language' : self.Language,
              'Place'    : self.Place,
              'UserLocation': self.UserLocation,
              'RetweetCount': self.RetweetCount,
              'Sentiment'   : self.Sentiment,
              'Polarity'    : self.Polarity,
              'id'       : self.id, 
              'Text'        : self.Text,
        }
# 
engine = create_engine('postgresql://ankit:chhewang@localhost/twitter')
Base.metadata.create_all(engine)