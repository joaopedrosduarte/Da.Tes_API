from sqlalchemy.sql.sqltypes import Integer, String, BigInteger, DateTime, Date, Boolean
from sqlalchemy import Table, Column
from config.db import meta
from datetime import datetime 

startupDB = Table(
    'startup', meta,
    Column('company_id', BigInteger, primary_key=True, nullable=False),
    Column('created_at', DateTime, default=datetime.now(),nullable=False),
    Column('updated_at', DateTime, default=datetime.now(), nullable=False),
    Column('deleted_at', DateTime, nullable=True),
    Column('contact_name', String(255), nullable=False),
    Column('representative_charge', String(255), nullable=False),
    Column('company_name', String(255), nullable=False),
    Column('email', String(255), nullable=False),
    Column('founded_at', Date, nullable=False),
    Column('city_and_state', String(255), nullable=False),
    Column('cnpj', String(255), nullable=False),
    Column('employees_count', Integer, nullable=False),
    Column('company_maturity', String(255), nullable=False),
    Column('company_segment', String(255), nullable=False),
    Column('company_monetization', String(255), nullable=False),
    Column('business_model', String(255), nullable=False),
    Column('mrr_income_6m', String(255), nullable=False)
)

#Column('esg', Boolean, nullable=False, default=0),
#Column('girl_power', Boolean, nullable=False, default=0)
    