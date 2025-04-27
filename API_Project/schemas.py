""" 
Contains Pydantic models used for API request and response validation.
Defines schemas for hotel management system entities such as Hotel, Room, Guest, Booking, and Service.
"""

from datetime import date
from typing import Optional
from pydantic import BaseModel

# Hotel Schemas
#Base schema for a hotel containing common fields
class HotelBase(BaseModel):
    name: str
    address: str
    city: str

#Schema for creating a new hotel
class HotelCreate(HotelBase):
    pass

#Schema for updating an existing hotel.
class HotelUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None

#Schema for returning hotel data
class HotelResponse(HotelBase):
    id: int

    class Config:
        orm_mode = True  # Enables ORM model parsing(JSON format)

# Room Schemas
#Base schema for a room containing common fields
class RoomBase(BaseModel):
    room_number: str
    room_type: str
    price_per_night: int
    hotel_id: int

#Schema for creating a new room
class RoomCreate(RoomBase):
    pass

#Schema for updating an existing room
class RoomUpdate(BaseModel):
    room_number: Optional[str] = None
    room_type: Optional[str] = None
    price_per_night: Optional[str] = None
    hotel_id: Optional[str] = None

#Schema for returning room data
class RoomResponse(RoomBase):
    id: int

    class Config:
        orm_mode = True # Enables ORM model parsing(JSON format)

# Guest Schemas
#Base schema for a guest containing common fields
class GuestBase(BaseModel):
    first_name: str
    last_name: str
    phone_number: str

#Schema for creating a new guest
class GuestCreate(GuestBase):
    pass

#Schema for updating an existing guest
class GuestUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[str] = None

#Schema for returning guest data
class GuestResponse(GuestBase):
    id: int

    class Config:
        orm_mode = True # Enables ORM model parsing(JSON format)

# Booking Schemas
#Base schema for a booking containing common fields
class BookingBase(BaseModel):
    guest_id: int
    room_id: int
    check_in_date: date
    check_out_date: date

#Schema for creating a new booking
class BookingCreate(BookingBase):
    pass

#Schema for updating an existing booking
class BookingUpdate(BaseModel):
    guest_id: Optional[str] = None
    room_id: Optional[str] = None
    check_in_date: Optional[str] = None
    check_out_date: Optional[str] = None

#Schema for returning booking data
class BookingResponse(BookingBase):
    id: int

    class Config:
        orm_mode = True  # Enables ORM model parsing(JSON format

# Service Schemas
#Base schema for a service containing common fields
class ServiceBase(BaseModel):
    name: str
    description: Optional[str] = None

#Schema for creating a new service
class ServiceCreate(ServiceBase):
    pass

#Schema for updating an existing service
class ServiceUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

#Schema for returning service data
class ServiceResponse(ServiceBase):
    id: int

    class Config:
        orm_mode = True  # Enables ORM model parsing(JSON format
