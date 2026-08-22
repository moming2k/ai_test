from app.models import Order, User

# In-memory "database" for the exercise. Kept intentionally simple —
# no ORM/session layer, so candidates can focus on the feature, not the plumbing.

USERS: list[User] = [
    User(id=1, name="Ada Lovelace", email="ada@example.com"),
    User(id=2, name="Grace Hopper", email="grace@example.com"),
    User(id=3, name="Alan Turing", email="alan@example.com"),
]

ORDERS: list[Order] = [
    Order(id=1, user_id=1, item="Mechanical Keyboard", quantity=1, status="delivered"),
    Order(id=2, user_id=1, item="USB-C Hub", quantity=2, status="shipped"),
    Order(id=3, user_id=2, item="Monitor Stand", quantity=1, status="pending"),
    Order(id=4, user_id=3, item="Webcam", quantity=1, status="pending"),
]
