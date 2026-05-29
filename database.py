
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



#everytime we connect to something that is one session
#like if we connect to the server or database that is one session.

db_url = "postgresql://postgres:12345678@localhost:5432/teluso"

engine = create_engine(db_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)