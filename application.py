import logging

from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from address import crud, model, schema

from db.db_handler import session_local, engine

model.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Address Details",
    description="You can perform CRUD operation by using this API",
    version="1.0.0"
)

logging.basicConfig(
    level=logging.DEBUG,
    format="{asctime} {levelname:<8} {message}",
    style='{',
    filename="logs/request.log",
    filemode='a'
)


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()


@app.get("/retrieve_all_address_details", response_model=List[schema.Address])
async def retrieve_all_address_details(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    addresses = crud.get_addresses(db=db, skip=skip, limit=limit)
    return addresses


@app.post("/add_new_address", response_model=schema.AddressAdd)
async def add_new_address(address: schema.AddressAdd, db: Session = Depends(get_db)):
    address_id = crud.get_address_by_address_id(db=db, address_id=address.address_id)
    if address_id:
        logging.error(f"Address details couldn't add to db due to address_id {address.address_id} is already exist")
        raise HTTPException(status_code=400, detail=f"Address detail with address_id {address.address_id} already "
                                                    f"exist in database.")
    return crud.add_address_details_to_db(db=db, address=address)


@app.delete("/delete_address_by_id")
async def delete_address_by_id(sl_id: int, db: Session = Depends(get_db)):
    details = crud.get_address_by_id(db=db, sl_id=sl_id)
    if not details:
        raise HTTPException(status_code=400, detail=f"No record found to delete")

    try:
        crud.delete_address_details_by_id(db=db, sl_id=sl_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")
    return {"delete status": "success"}


@app.put('/update_address_details', response_model=schema.Address)
async def update_address_details(sl_id: int, update_param: schema.UpdateAddress, db: Session = Depends(get_db)):
    details = crud.get_address_by_id(db=db, sl_id=sl_id)
    if not details:
        raise HTTPException(status_code=400, detail=f"No record found to delete")
    return crud.update_address_details(db=db, details=update_param, sl_id=sl_id)
