from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Crud.room_crud import room_crud
from schemas import RoomCreate, RoomUpdate, RoomResponse
from typing import List
from database import get_db

# Router for handling room-related API requests
router = APIRouter(
    prefix="/rooms", # API endpoint prefix
    tags=["Rooms"] # Tag for the bookings endpoint group
)

# Route for creating a room
@router.post("/", response_model=RoomResponse,summary="Oda oluştur",description="Yeni bir oda kaydı oluşturur ve veritabanına ekler.",response_description="Oluşturulan odanın bilgileri döndürülür.")
def create_room(room: RoomCreate, db: Session = Depends(get_db)):
    return room_crud.create_item(schema=room,db=db)

# Route for reading all rooms
@router.get("/", response_model=List[RoomResponse],summary="Tüm odaları getir",description="Veritabanındaki tüm oda kayıtlarını listeler.",response_description="Oda kayıtlarının listesi döndürülür.")
def read_rooms(db: Session = Depends(get_db), skip: int = 0, limit: int = 100,):
    return room_crud.read_items(db=db, skip=skip, limit=limit)

# Route for reading a single room by its ID
@router.get("/{room_id}", response_model=RoomResponse,summary="Oda bilgisi getir",description="Belirtilen ID'ye sahip odanın bilgilerini getirir.",response_description="İstenen odanın bilgileri döndürülür.")
def read_room(room_id: int, db: Session = Depends(get_db)):
    return room_crud.read_item(db=db, item_id= room_id)

# Route for updating a room's details
@router.put("/{room_id}", response_model=RoomResponse,summary="Oda bilgilerini güncelle",description="Belirtilen ID'ye sahip odanın bilgilerini günceller.",response_description="Güncellenmiş oda bilgileri döndürülür.")
def update_room(room_id: int, room: RoomUpdate, db: Session = Depends(get_db)):
    return room_crud.update_item(schema=room, db=db, item_id=room_id)

# Route for deleting a room by its ID
@router.delete("/{room_id}", response_model=RoomResponse,summary="Oda sil",description="Belirtilen ID'ye sahip oda kaydını veritabanından siler.",response_description="Silinen odanın bilgileri döndürülür.")
def delete_room(room_id: int, db: Session = Depends(get_db)):
    return room_crud.delete_item(db=db, item_id= room_id)
