from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Customer(BaseModel):
    fullName: str

class Order(BaseModel):
    id: int
    customer: Customer 
    totalAmount: float   
data = [
  {
    "id": 1,
    "customer": {
      "fullName": "Anna Smith"
    },
    "totalAmount": 99.9
  },
  {
    "id": 2,
    "customer": {
      "fullName": "John Doe"
    },
    "totalAmount": 250.0
  },
  {
    "id": 3,
    "customer": {
      "fullName": "Maria Garcia"
    },
    "totalAmount": 0.0
  }
]
@app.get("/customers/{customer_id}")
def get_customer(customer_id: int)-> Order:
    for customer in data:
            if customer_id == customer["id"]:
                return customer
    raise HTTPException(status_code=404, detail="User not found")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("providers.v2:app", host="127.0.0.1", port=8002, reload=True)