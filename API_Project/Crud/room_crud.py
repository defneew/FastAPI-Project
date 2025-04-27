from Crud.crud import CrudBase
from database import Room
from schemas import RoomCreate

#Create a crud class for room by inheriting the CrudBase class
class CrudRoom(CrudBase[Room, RoomCreate]):
    pass

room_crud = CrudRoom(Room) #Derive object from CrudRoom class