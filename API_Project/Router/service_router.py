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
@router.post("/", response_model=ServiceResponse)
def create_service(service: ServiceCreate, db: Session = Depends(get_db)):
    return service_crud.create_item(schema=service,db=db)

# Route for reading all services
@router.get("/", response_model=List[ServiceResponse])
def read_services(db: Session = Depends(get_db), skip: int = 0, limit: int = 100,):
    return service_crud.read_items(db=db, skip=skip, limit=limit)

# Route for reading a single service by its ID
@router.get("/{service_id}", response_model=ServiceResponse)
def read_service(service_id: int, db: Session = Depends(get_db)):
    return service_crud.read_item(db=db, item_id= service_id)

# Route for updating a service's detail
@router.put("/{service_id}", response_model=ServiceResponse)
def update_service(service_id: int, service: ServiceUpdate, db: Session = Depends(get_db)):
    return service_crud.update_item(schema=service, db=db, item_id=service_id)

# Route for deleting a service by its ID
@router.delete("/{service_id}", response_model=ServiceResponse)
def delete_service(service_id: int, db: Session = Depends(get_db)):
    return service_crud.delete_item(db=db, item_id= service_id)
