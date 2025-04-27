from Crud.crud import CrudBase
from database import Service
from schemas import ServiceCreate

#Create a crud class for service by inheriting the CrudBase class
class CrudService(CrudBase[Service, ServiceCreate]):
    pass

service_crud = CrudService(Service)  #Derive object from CrudService class
