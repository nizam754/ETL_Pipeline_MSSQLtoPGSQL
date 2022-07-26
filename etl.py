#import needed libraries
from sqlalchemy import create_engine
import pyodbc
import pandas as pd
import os

#get password from environmnet var
pwd = os.environ['PGPASS']
uid = os.environ['PGUID']
#sql db details
driver = "{SQL Server Native Client 11.0}"
server = "haq-PC"
database = "AdventureWorks2017;"

