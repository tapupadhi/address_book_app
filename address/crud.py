from sqlalchemy.orm import Session
from address import model, schema


def get_address_by_address_id(db: Session, address_id: str):
    return db.query(model.Address).filter(model.Address.address_id == address_id).first()


def get_address_by_id(db: Session, sl_id: int):
    return db.query(model.Address).filter(model.Address.id == sl_id).first()


def get_addresses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Address).offset(skip).limit(limit).all()


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
    return model.Address(**address.dict())


def update_address_details(db: Session, sl_id: int, details: schema.UpdateAddress):
    db.query(model.Address).filter(model.Address.id == sl_id).update(vars(details))
    db.commit()
    return db.query(model.Address).filter(model.Address.id == sl_id).first()


def delete_address_details_by_id(db: Session, sl_id: int):
    try:
        db.query(model.Address).filter(model.Address.id == sl_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)
