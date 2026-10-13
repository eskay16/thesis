from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()

class User(BaseModel):
    id: int
    customer_name: str
    amount: float

users = [
  {
    "id": 1,
    "customer_name": "Anna Smith",
    "amount": 99.9
  },
  {
    "id": 2,
    "customer_name": "John Doe",
    "amount": 250.0
  },
  {
    "id": 3,
    "customer_name": "Maria Garcia",
    "amount": 0.0
  }
]



@app.get("/users/{user_id}")
def get_user(user_id: int) -> User:
    for element in users:
        if user_id == element["id"]:
            return element
    raise HTTPException(status_code=404, detail="User not found")


