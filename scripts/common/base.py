# Import the modules required
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base

# Create the engine
# Use login credentials on the database profile user1, user1
engine = create_engine(
    "postgresql+psycopg2://user1:user1@localhost:5432/postgres"
    )
print(engine.url)
# Initialize the session
session = Session(engine)

# Initialize the declarative base to inherit from
Base = declarative_base()
