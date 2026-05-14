from sqlalchemy import Column, Integer, String
from app.database.db import Base

class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    url = Column(String)
    status = Column(String)