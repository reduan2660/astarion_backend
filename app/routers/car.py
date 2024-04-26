from fastapi import HTTPException, Depends, APIRouter, Query
from fastapi.params import Body
from ..database import get_db
from sqlalchemy.orm import Session
from ..schemas import User, ResponseUser, Car
from passlib.context import CryptContext
from typing import List
from .. import models, oauth2, utils

router = APIRouter(
    tags=['cars'],
    prefix="/cars"
)

@router.post("/", status_code = 201)
def create_car(car : Car, db : Session = Depends(get_db), user : User = Depends(oauth2.get_current_user)) :
    new_car = models.Car(**car.dict())
    print(user.id)
    new_car.owner_id = user.id
    print(new_car)
    
    db.add(new_car)
    db.commit()
    db.refresh(new_car)
    return new_car

@router.get("/all", response_model=List[Car])
def get_cars(db : Session = Depends(get_db)) :
    cars = db.query(models.Car).all()
    return cars

@router.get("/mycars", response_model = List[Car])
def get_mycars(db : Session = Depends(get_db), user : User = Depends(oauth2.get_current_user)) :
    cars = db.query(models.Car).filter(models.Car.owner_id == user.id).all()
    return cars






















@router.get("/{car_id}", response_model = Car)
def get_cars(car_id : int, db : Session = Depends(get_db)) :
    car = db.query(models.Car).filter(models.Car.id == car_id).first()
    return car

