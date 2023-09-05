from sqlalchemy import create_engine
from os import environ
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

load_dotenv()

Base = declarative_base()

engine = create_engine(environ.get('DATABASE_URI_PROD'), echo=True)
Session = sessionmaker(bind=engine)
session = Session()