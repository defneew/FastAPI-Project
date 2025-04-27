from Crud.crud import CrudBase
from database import Guest
from schemas import GuestCreate

#Create a crud class for guest by inheriting the CrudBase class
class CrudGuest(CrudBase[Guest, GuestCreate]):
    pass

guest_crud = CrudGuest(Guest)  #Derive object from CrudGuest class