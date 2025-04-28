from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Crud.booking_crud import booking_crud
from schemas import BookingCreate, BookingUpdate, BookingResponse
from typing import List
from database import get_db

# Router for handling booking-related API requests
router = APIRouter(
    prefix="/bookings", # API endpoint prefix
    tags=["Bookings"] # Tag for the bookings endpoint group
)

# Route for creating a booking
@router.post("/", response_model=BookingResponse,summary="Rezervasyon oluştur",description="Yeni bir rezervasyon kaydı oluşturur ve veritabanına ekler.",response_description="Oluşturulan rezervasyonun bilgileri döndürülür.")
def create_booking(booking: BookingCreate, db: Session = Depends(get_db)):
    return booking_crud.create_item(schema=booking,db=db)

# Route for reading all bookings
@router.get("/", response_model=List[BookingResponse],summary="Tüm rezervasyonları getir",description="Veritabanındaki tüm rezervasyon kayıtlarını listeler.",response_description="Rezervasyon kayıtlarının listesi döndürülür.")
def read_bookings(db: Session = Depends(get_db), skip: int = 0, limit: int = 100,):
    return booking_crud.read_items(db=db, skip=skip, limit=limit)

# Route for reading a single booking by its ID
@router.get("/{booking_id}", response_model=BookingResponse,summary="Rezervasyon bilgisi getir",description="Belirtilen ID'ye sahip rezervasyonun bilgilerini getirir.",response_description="İstenen rezervasyonun bilgileri döndürülür.")
def read_booking(booking_id: int, db: Session = Depends(get_db)):
    return booking_crud.read_item(db=db, item_id= booking_id)

# Route for updating a booking's details
@router.put("/{booking_id}", response_model=BookingResponse,summary="Rezervasyon bilgilerini güncelle",description="Belirtilen ID'ye sahip rezervasyonun bilgilerini günceller.",response_description="Güncellenmiş rezervasyon bilgileri döndürülür.")
def update_booking(booking_id: int, booking: BookingUpdate, db: Session = Depends(get_db)):
    return booking_crud.update_item(schema=booking, db=db, item_id=booking_id)

# Route for deleting a booking by its ID
@router.delete("/{booking_id}", response_model=BookingResponse,summary="Rezervasyon sil",description="Belirtilen ID'ye sahip rezervasyon kaydını veritabanından siler.",response_description="Silinen rezervasyonun bilgileri döndürülür.")
def delete_booking(booking_id: int, db: Session = Depends(get_db)):
    return booking_crud.delete_item(db=db, item_id= booking_id)
