from sqlite3 import DatabaseError
from fastapi import FastAPI
from redis_om import get_redis_connection, HashModel

app = FastAPI()

redis = get_redis_connection(
    host="redis-16337.c301.ap-south-1-1.ec2.cloud.redislabs.com",
    port="16337",
    password="KU17wk6VZw2c0gwekQDdJLLBh3uI0Tna",
    decode_responses = True,
)

class Product(HashModel):
    name: str
    price: float
    quantity: int

    class Meta:
        database = redis 


@app.get("/products")
def all():
    return [];
