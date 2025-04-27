from sqlalchemy import create_engine, Table, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from fastapi import FastAPI
import os


app = FastAPI()

DATABASE_URL = "sqlite:///./.hotel.db"  #database name

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit= False, autoflush=False, bind=engine)

Base = declarative_base()

#many to many relationship (between room and service)
room_service_association = Table(
    "room_service_association",
    Base.metadata,
    Column("room_id", Integer, ForeignKey("tb_rooms.id")),
    Column("service_id",Integer, ForeignKey("tb_services.id"))
)
#Hotel table
class Hotel(Base):
    __tablename__ = "tb_hotels"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,nullable=False)
    address = Column(String, nullable=False)
    city = Column(String, nullable=False)

#Room table
class Room(Base):
    __tablename__ = "tb_rooms"

    id = Column(Integer, primary_key=True, index=True)
    room_number = Column(String,nullable=False)
    room_type = Column(String, nullable=False)
    price_per_night = Column(Integer, nullable=False)
    hotel_id = Column(Integer, ForeignKey("tb_hotels.id")) #Hotel information is linked to the room table with a foreign key.

    #one to many relationship(between room and hotel)
    hotel = relationship("Hotel", backref = "rooms")
    #many to many relationship(between room and service)
    services = relationship("Service", secondary=room_service_association, back_populates="rooms")

#Guest table
class Guest(Base):
    __tablename__ = "tb_guests"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone_number = Column(String, unique=True, nullable=False)

#Booking table
class Booking(Base):
    __tablename__ = "tb_bookings"

    id = Column(Integer, primary_key=True, index=True)
    guest_id = Column(Integer, ForeignKey("tb_guests.id")) #Guest information is linked to the booking table with a foreign key.
    room_id = Column(Integer, ForeignKey("tb_rooms.id")) #Room information is linked to the booking table with a foreign key.
    check_in_date = Column(Date, nullable=False)
    check_out_date = Column(Date, nullable=False)

    #one to many relationship(between booking and guest)
    guest = relationship("Guest", backref="bookings")
    #one to many relationship(between booking and room)
    room = relationship("Room", backref="bookings")

#Service table
class Service(Base):
    __tablename__ = "tb_services"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    #many to many relationship(between room and service)
    rooms = relationship("Room", secondary=room_service_association, back_populates="services")

#database connection
def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close() 

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine) #create database
