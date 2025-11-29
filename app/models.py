from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Course(Base):
  __tablename__= "courses"

  id = Column(Integer, primary_key=True, index=True)
  title = Column(String, nullable=False)
  author = Column(String, nullable=False)
  price = Column(Float, nullable=False)
  image = Column(String, nullable=False)