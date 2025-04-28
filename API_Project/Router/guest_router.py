from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Crud.guest_crud import guest_crud
from schemas import GuestCreate, GuestUpdate, GuestResponse
from typing import List
from database import get_db

# Router for handling guest-related API requests
router = APIRouter(
    prefix="/guests",
    tags=["Guests"]
)

# Route for creating a guest
@router.post("/", response_model=GuestResponse,summary="Misafir oluştur",description="Yeni bir misafir kaydı oluşturur ve veritabanına ekler.",response_description="Oluşturulan misafirin bilgileri döndürülür.")
def create_guest(guest: GuestCreate, db: Session = Depends(get_db)):
    return guest_crud.create_item(schema=guest,db=db)

# Route for reading all guests
@router.get("/", response_model=List[GuestResponse],summary="Tüm misafirleri getir",description="Veritabanındaki tüm misafir kayıtlarını listeler.",response_description="Misafir kayıtlarının listesi döndürülür.")
def read_guests(db: Session = Depends(get_db), skip: int = 0, limit: int = 100,):
    return guest_crud.read_items(db=db, skip=skip, limit=limit)

# Route for reading a single guest by its ID
@router.get("/{guest_id}", response_model=GuestResponse,summary="Misafir bilgisi getir",description="Belirtilen ID'ye sahip misafirin bilgilerini getirir.",response_description="İstenen misafirin bilgileri döndürülür.")
def read_guest(guest_id: int, db: Session = Depends(get_db)):
    return guest_crud.read_item(db=db, item_id= guest_id)

# Route for updating a guest's details
@router.put("/{guest_id}", response_model=GuestResponse,summary="Misafir bilgilerini güncelle",description="Belirtilen ID'ye sahip misafirin bilgilerini günceller.",response_description="Güncellenmiş misafir bilgileri döndürülür.")
def update_guest(guest_id: int, guest: GuestUpdate, db: Session = Depends(get_db)):
    return guest_crud.update_item(schema=guest, db=db, item_id=guest_id)

# Route for deleting a guest by its ID
@router.delete("/{guest_id}", response_model=GuestResponse,summary="Misafir sil",description="Belirtilen ID'ye sahip misafir kaydını veritabanından siler.",response_description="Silinen misafirin bilgileri döndürülür.")
def delete_guest(guest_id: int, db: Session = Depends(get_db)):
    return guest_crud.delete_item(db=db, item_id= guest_id)
