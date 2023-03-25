from typing import Optional
from pydantic import BaseModel, Field, PositiveInt, validator, constr


class AddressBase(BaseModel):
    address_line1: constr(max_length=50)
    address_line2: Optional[constr(max_length=50)] = None
    state: constr(max_length=50)
    city: constr(max_length=30)
    pincode: PositiveInt
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)

    @validator("pincode")
    def pincode_length(cls, v):
        if len(str(v)) != 6:
            raise ValueError("Pincode must be of six digits")
        return v


class AddressAdd(AddressBase):
    address_id: str

    class Config:
        orm_mode = True


class Address(AddressAdd):
    id: int

    class Config:
        orm_mode = True


class UpdateAddress(BaseModel):
    address_line1: str
    address_line2: Optional[str] = None
    state: str
    city: str
    pincode: PositiveInt
    latitude: float
    longitude: float

    class Config:
        orm_mode = True
