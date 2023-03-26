from sqlalchemy.orm import Session
from address import model, schema

import logging


def get_address_by_address_id(db: Session, address_id: str):
    record = db.query(model.Address).filter(model.Address.address_id == address_id).first()
    logging.info(f"Address record fetched from DB based with address_id {address_id} successfully.")
    return record


def get_address_by_id(db: Session, sl_id: int):
    record = db.query(model.Address).filter(model.Address.id == sl_id).first()
    logging.info(f"Address record fetched from DB with id {sl_id} successfully.")
    return record


def get_addresses(db: Session, skip: int = 0, limit: int = 100):
    records = db.query(model.Address).offset(skip).limit(limit).all()
    logging.info("Address records fetched from DB successfully.")
    return records


def add_address_details_to_db(db: Session, address: schema.AddressAdd):
    address_details = model.Address(
        address_id=address.address_id,
        address_line1=address.address_line1,
        address_line2=address.address_line2,
        state=address.state,
        city=address.city,
        pincode=address.pincode,
        latitude=address.latitude,
        longitude=address.longitude
    )
    db.add(address_details)
    db.commit()
    db.refresh(address_details)
    logging.info(f"Address details with address_id {address.address_id} got added to db successfully.")
    return model.Address(**address.dict())


def update_address_details(db: Session, sl_id: int, details: schema.UpdateAddress):
    db.query(model.Address).filter(model.Address.id == sl_id).update(vars(details))
    db.commit()
    logging.info(f"Address details with id {sl_id} got updated successfully.")
    return db.query(model.Address).filter(model.Address.id == sl_id).first()


def delete_address_details_by_id(db: Session, sl_id: int):
    try:
        db.query(model.Address).filter(model.Address.id == sl_id).delete()
        db.commit()
        logging.info(f"Address details with id {sl_id} got deleted successfully.")
    except Exception as e:
        logging.error("At the time of deleting: ", str(e))
        raise Exception(e)
