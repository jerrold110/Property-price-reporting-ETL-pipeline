## Property price reporting ETL pipeline
This project contains the code for an ETL pipeline that downloads zip files from an API endpoint, transforms the data, and stores it in a Postgres database using Python and Sqlalchemy. The table structures for storing raw and clean data as well as other components to interact with the Database are defined under the common folder, create_tables.py has to be run after setting up the postgres database, before running execute.py.

#### Extract
- Sends get request
- Downloads zip file and unzips into csv

#### Transform
- Creates engine and session to intereact with postgres
- Create table classes with unique row identifiers
- Reads data fron csv file, cleans data, writes to tables
- Load tables into database

#### Load
- Query rows in ppr_raw that are not in ppr_clean to discover new rows
- Cleans data into new format
- Load data into tables
- Delete leftover rows in ppr_raw that could not be transformed