from fastapi import FastAPI
from Router import hotel_router,room_router,guest_router,booking_router,service_router

# Initializing the FastAPI application
app = FastAPI()

app.include_router(hotel_router.router) # Including the hotel router in the app
app.include_router(room_router.router) # Including the room router in the app
app.include_router(guest_router.router) # Including the guest router in the app
app.include_router(booking_router.router) # Including the booking router in the app
app.include_router(service_router.router) # Including the service router in the app
