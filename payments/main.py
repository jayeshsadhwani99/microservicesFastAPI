from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, HashModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*" ],
    allow_headers=["*"],
)

# Another DB (for microservices architecture)
redis = get_redis_connection(
    host="redis-16337.c301.ap-south-1-1.ec2.cloud.redislabs.com",
    port="16337",
    password="KU17wk6VZw2c0gwekQDdJLLBh3uI0Tna",
    decode_responses = True,
)