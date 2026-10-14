import httpx


BASE_URL = "http://127.0.0.1:8002"   
PATH = "/users/1"  

response = httpx.get(BASE_URL + PATH)
response.raise_for_status()
data = response.json()
print(data["customer_name"], data["amount"])



