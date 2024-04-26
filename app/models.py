from .database import Base
from sqlalchemy import Integer, Boolean, String, Column, ForeignKey, Float, LargeBinary
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship

class User(Base) :
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String, nullable=True)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    is_verified = Column(Boolean, nullable=False, default=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    role = Column(String, nullable=False, default="customer")

    
    


class Car(Base) :
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    model = Column(String, nullable=True)
    year = Column(Integer, nullable = True)
    description = Column(String, nullable = True)
    price = Column(Float, nullable = False)
    image_data = Column(LargeBinary, nullable = True, default=None)
    image_url = Column(String, nullable = True)
    owner_id = Column(Integer, ForeignKey("users.id"))  
    sold = Column(Boolean, nullable = False, default=False)
    owner = relationship("User")

class CarSellOffer(Base) :
    __tablename__ = "car_sell_offers"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    car_id = Column(Integer, ForeignKey("cars.id"))
    offer_price = Column(Float, nullable = False)
    buyer_id = Column(Integer, ForeignKey("users.id"))
    status = Column(String, nullable = False, default="pending")
    car = relationship("Car")
    buyer = relationship("User")