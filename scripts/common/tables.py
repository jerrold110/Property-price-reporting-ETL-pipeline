import os
import sys
# Add current directory to path
absolute_path = os.path.dirname(__file__)
sys.path.append(absolute_path)

from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import cast
from sqlalchemy.orm import column_property
from base import Base

# all tables inherit from declarative base class
# These are the tables to create

class PprRawAll(Base):
    __tablename__ = 'ppr_raw_all'
    id = Column(Integer, primary_key=True)
    date_of_sale = Column(String(55))
    address = Column(String(255))
    postal_code = Column(String(55))
    county = Column(String(55))
    price = Column(String(55))
    description = Column(String(55))
    
    transaction_id = column_property(
        date_of_sale + "_" + address + "_" + county + "_" + price
    )
    
class PprCleanAll(Base):
    __tablename__ = "ppr_clean_all"
	
	# date_of_sale is changed to Date, price is changed to Integer
    id = Column(Integer, primary_key=True)
    date_of_sale = Column(Date)
    address = Column(String(255))
    postal_code = Column(String(55))
    county = Column(String(55))
    price = Column(Integer)
    description = Column(String(255))
    # transaction_id has to be cast as a complete string
    transaction_id = column_property(
        cast(date_of_sale, String) + "_" + address + "_" + county + "_" + cast(price, String)
    )
