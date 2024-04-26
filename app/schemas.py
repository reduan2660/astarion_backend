from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date


class User(BaseModel) :
    name : str
    email : EmailStr
    phone : str
    password : str
    role : Optional[str] = "customer"
    
    class Config :
        orm_mode = True
     
class UpdateUser(BaseModel) :
    name : str
    phone : str
    
        
class ResponseUser(BaseModel) :
    name : str
    phone : str
    email : EmailStr
    role : str

    class Config :
        orm_mode = True
        
class UserLogin(BaseModel) :
    username : EmailStr
    password : str

class Token(BaseModel) :
    access_token : str
    token_type : str

class TokenData(BaseModel) :
    id : int 
    email : str

class Car(BaseModel) :
    model : str | None = None
    year : int | None = None
    description : str | None = None
    price : float
    image_data : bytes | None = None
    image_url : str | None = None
    owner_id : int | None = None
    sold : bool | None = False
    
    class Config :
        orm_mode = True
        
class CarSellOffer(BaseModel) :
    id : int | None = None
    car_id : int
    offer_price : float
    status : str | None = "pending"
    buyer_id : int | None = None