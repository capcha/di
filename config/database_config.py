from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool

conn_string = "postgresql://postgres:123@localhost/"
engine = create_engine(conn_string, pool=NullPool)
