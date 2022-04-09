import uuid
from typing import List, Optional
from uuid import UUID

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

from utils.exception import NegativeValueException

router: APIRouter = APIRouter(prefix="/products")

PRODUCTS: List = []


class Product(BaseModel):
    id: UUID
    product_name: str = Field(min_length=1)
    brand: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(max_length=255, min_length=1)
    price: int = Field(gt=-1, lt=100000)

    class Config:
        schema_extra = {
            "example": {
                "id": "ee1a7f3c-3a50-4550-9103-2992cc82361c",
                "product_name": "iPhone 13 Pro 128GB Silver",
                "brand": "Apple",
                "description": "Description of iPhone 13 Pro 128GB Silver",
                "price": 37000,
            }
        }


class ProductCreate(BaseModel):
    product_name: str = Field(min_length=1)
    brand: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(max_length=255, min_length=1)
    price: int = Field(gt=-1, lt=100000)

    class Config:
        schema_extra = {
            "example": {
                "product_name": "iPhone 13 Pro 128GB Silver",
                "brand": "Apple",
                "description": "Description of iPhone 13 Pro 128GB Silver",
                "price": 37000,
            }
        }


@router.get("", response_model=List[Product])
async def get_product_list(limit: Optional[int] = None):
    if limit and limit < 0:
        raise NegativeValueException(message="Limit must be positive number")
    if limit:
        return PRODUCTS[:limit]
    else:
        return PRODUCTS


@router.get("/{product_id}", response_model=Product)
async def get_product_by_id(product_id: UUID):
    for product in PRODUCTS:
        if product.id == product_id:
            return product
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Product not found",
    )


@router.post("", status_code=status.HTTP_201_CREATED, response_model=Product)
async def create_product(product: ProductCreate):
    product_param = product.dict()
    product_param["id"] = str(uuid.uuid4())
    product_resp = Product(**product_param)
    PRODUCTS.append(product_resp)
    return product_resp


def create_products():
    PRODUCTS.append(
        Product(
            id=str(uuid.uuid4()),
            product_name="Samsung Galaxy Z Flip3 128GB",
            brand="Samsung",
            description="Description of Samsung Galaxy Z Flip3 128GB",
            price=29000,
        )
    )
    PRODUCTS.append(
        Product(
            id=str(uuid.uuid4()),
            product_name="Samsung Galaxy Z Flip3 256GB",
            brand="Samsung",
            description="Description of Samsung Galaxy Z Flip3 256GB",
            price=31000,
        )
    )
    PRODUCTS.append(
        Product(
            id=str(uuid.uuid4()),
            product_name="iPhone 13 Pro 128GB",
            brand="Apple",
            description="Description of Apple 13 Pro 128GB",
            price=27000,
        )
    )
    PRODUCTS.append(
        Product(
            id=str(uuid.uuid4()),
            product_name="iPhone 13 Pro 256GB",
            brand="Apple",
            description="Description of Apple 13 Pro 256GB",
            price=42000,
        )
    )


create_products()
