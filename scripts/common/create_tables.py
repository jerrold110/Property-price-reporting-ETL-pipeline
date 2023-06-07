from base import Base, engine
from tables import PprRawAll, PprCleanAll

print('Printing all tables in base.metadata.tables')
for table in Base.metadata.tables:
    print(table)

# Create the tables in the database
# Create all descendents of Base (pprrawall and pprcleanall)
Base.metadata.create_all(engine)

