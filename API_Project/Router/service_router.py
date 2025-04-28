from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Crud.service_crud import service_crud
from schemas import ServiceCreate, ServiceUpdate, ServiceResponse
from typing import List
from database import get_db

router = APIRouter(
    prefix="/services",
    tags=["Services"]
)

# Route for creating a service
@router.post("/", response_model=ServiceResponse,summary="Servis oluştur",description="Yeni bir servis kaydı oluşturur ve veritabanına ekler.",response_description="Oluşturulan servisin bilgileri döndürülür.")
def create_service(service: ServiceCreate, db: Session = Depends(get_db)):
    return service_crud.create_item(schema=service,db=db)

# Route for reading all services
@router.get("/", response_model=List[ServiceResponse],summary="Tüm servisleri getir",description="Veritabanındaki tüm servis kayıtlarını listeler.",response_description="Servis kayıtlarının listesi döndürülür.")
def read_services(db: Session = Depends(get_db), skip: int = 0, limit: int = 100,):
    return service_crud.read_items(db=db, skip=skip, limit=limit)

# Route for reading a single service by its ID
@router.get("/{service_id}", response_model=ServiceResponse,summary="Servis bilgisi getir",description="Belirtilen ID'ye sahip servisin bilgilerini getirir.",response_description="İstenen servisin bilgileri döndürülür.")
def read_service(service_id: int, db: Session = Depends(get_db)):
    return service_crud.read_item(db=db, item_id= service_id)

# Route for updating a service's detail
@router.put("/{service_id}", response_model=ServiceResponse,summary="Servis bilgilerini güncelle",description="Belirtilen ID'ye sahip servisin bilgilerini günceller.",response_description="Güncellenmiş servis bilgileri döndürülür.")
def update_service(service_id: int, service: ServiceUpdate, db: Session = Depends(get_db)):
    return service_crud.update_item(schema=service, db=db, item_id=service_id)

# Route for deleting a service by its ID
@router.delete("/{service_id}", response_model=ServiceResponse,summary="Servis sil",description="Belirtilen ID'ye sahip servis kaydını veritabanından siler.",response_description="Silinen servisin bilgileri döndürülür.")
def delete_service(service_id: int, db: Session = Depends(get_db)):
    return service_crud.delete_item(db=db, item_id= service_id)
