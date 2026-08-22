from fastapi import APIRouter, HTTPException

from app.data import ORDERS, USERS
from app.models import Order

router = APIRouter(prefix="/orders", tags=["orders"])


@router.get("", response_model=list[Order])
def list_orders() -> list[Order]:
    return ORDERS


@router.get("/{order_id}", response_model=Order)
def get_order(order_id: int) -> Order:
    for order in ORDERS:
        if order.id == order_id:
            return order
    raise HTTPException(status_code=404, detail="Order not found")


@router.get("/by-user/{user_id}", response_model=list[Order])
def get_orders_for_user(user_id: int) -> list[Order]:
    if not any(u.id == user_id for u in USERS):
        raise HTTPException(status_code=404, detail="User not found")
    return [order for order in ORDERS if order.user_id == user_id]
