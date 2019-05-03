import json

from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.types import DateTime

#import TEST

class Items(Base):
    """
    Items table
    """
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    quantity = Column(Integer)
    description = Column(String(256))
    date_added = Column(DateTime())

    def __init__(self, name=None, quantity=None, description=None, date_added=None):
        self.name = name
        self.quantity = quantity
        self.description = description
        self.date_added = date_added

    def __repr__(self):
        rep = {'name': self.name,
        'quantity' : self.quantity,
        'description' : self.description,
        'data_added': self.date_added.strftime("%A, %d. %B %Y %I:%M%p")}
        rep = json.dumps(rep)
        return rep
        #return 'item %s' % (self.name)




