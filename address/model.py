from sqlalchemy import Boolean, Column, Integer, String, Float

from db.db_handler import Base


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    address_id = Column(String, unique=True, index=True, nullable=False)
    address_line1 = Column(String, nullable=False)
    address_line2 = Column(String)
    state = Column(String, nullable=False)
    city = Column(String, nullable=False)
    pincode = Column(Integer, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
