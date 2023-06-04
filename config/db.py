from sqlalchemy import create_engine, MetaData

db_url = f"mysql+mysqlconnector://admin:admin123456@database-cschool2023.cluster-c8hr0uqhzlcv.us-east-1.rds.amazonaws.com:3306/jpds"

engine = create_engine(db_url)
meta = MetaData()
con = engine.connect()