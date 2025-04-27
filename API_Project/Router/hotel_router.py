from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Crud.hotel_crud import hotel_crud
from schemas import HotelCreate, HotelUpdate, HotelResponse
from typing import List
from database import get_db

# Router for handling hotel-related API requests
router = APIRouter(
    prefix="/hotels", # API endpoint prefix
    tags=["Hotels"] # Tag for the bookings endpoint group
)

# Route for creating a hotel
@router.post("/", response_model=HotelResponse)
def create_hotel(hotel: HotelCreate, db: Session = Depends(get_db)):
    return hotel_crud.create_item(schema=hotel,db=db)

# Route for reading all hotels
@router.get("/", response_model=List[HotelResponse])
def read_hotels(db: Session = Depends(get_db), skip: int = 0, limit: int = 100,):
    return hotel_crud.read_items(db=db, skip=skip, limit=limit)

# Route for reading a single hotel by its ID
@router.get("/{hotel_id}", response_model=HotelResponse)
def read_hotel(hotel_id: int, db: Session = Depends(get_db)):
    return hotel_crud.read_item(db=db, item_id= hotel_id)

# Route for updating a hotel's details
@router.put("/{hotel_id}", response_model=HotelResponse)
def update_hotel(hotel_id: int, hotel: HotelUpdate, db: Session = Depends(get_db)):
    return hotel_crud.update_item(schema=hotel, db=db, item_id=hotel_id)

# Route for deleting a hotel by its ID
@router.delete("/{hotel_id}", response_model=HotelResponse)
def delete_hotel(hotel_id: int, db: Session = Depends(get_db)):
    return hotel_crud.delete_item(db=db, item_id= hotel_id)
