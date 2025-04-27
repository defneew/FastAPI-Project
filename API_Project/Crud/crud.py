from fastapi import HTTPException
from sqlalchemy.orm import Session
from typing import Type, TypeVar, Generic

Model = TypeVar("Model")  # Orm Model
Schema = TypeVar("Schema") #Schema type

#comman class for crud operation with model(Hotel,Room,Guest,Booking,Service)
class CrudBase(Generic[Model, Schema]):
    def __init__(self, model: Type[Model]):
        self.model = model #common (model name)

    #create function
    def create_item(self,schema: Schema, db: Session):  
        db_item = self.model(**schema.dict())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    #get function
    def read_items(self, db: Session, skip: int = 0, limit: int = 100): 
        return db.query(self.model).offset(skip).limit(limit).all()
    #get all function
    def read_item(self, db: Session, item_id:int): 
        item = db.query(self.model).filter(self.model.id == item_id).first()

        #If there is no item in the search criteria
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return item

    #update function
    def update_item(self, schema: Schema, db: Session, item_id: int): 
        item = db.query(self.model).filter(self.model.id == item_id).first()

        #If there is no item in the search criteria
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        for key, value in schema.dict(exclude_unset=True).items():
            setattr(item, key, value)
        db.commit()
        db.refresh(item)
        return item

    #delete function
    def delete_item(self, db: Session, item_id:int): 
        item = db.query(self.model).filter(self.model.id == item_id).first()

        #If there is no item in the search criteria
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        
        db.delete(item)
        db.commit()
        return item

