from Crud.crud import CrudBase
from database import Booking
from schemas import BookingCreate

#Create a crud class for booking by inheriting the CrudBase class
class CrudBooking(CrudBase[Booking, BookingCreate]):
    pass

booking_crud = CrudBooking(Booking)  #Derive object from CrudBooking class
