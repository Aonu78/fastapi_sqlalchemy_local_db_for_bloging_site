from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# engine = create_engine('sqlite:///./blog.db',echa=True)
SQLALCAMY_DATABASE_URL = 'sqlite:///./blog.db'
engine = create_engine(SQLALCAMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()
# 