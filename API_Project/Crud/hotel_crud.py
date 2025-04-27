from Crud.crud import CrudBase
from database import Hotel
from schemas import HotelCreate

#Create a crud class for hotel by inheriting the CrudBase class
class CrudHotel(CrudBase[Hotel, HotelCreate]):
    pass

hotel_crud = CrudHotel(Hotel) #Derive object from CrudHotel class
