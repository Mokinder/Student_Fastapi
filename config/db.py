from sqlalchemy import create_engine,MetaData

engine = create_engine('mysql+pymysql://root:9840581160@localhost:3306/demoDB')
meta=MetaData()

con=engine.connect()



