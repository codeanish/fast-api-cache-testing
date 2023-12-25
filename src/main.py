from fastapi import FastAPI
from requests import get
import redis

app = FastAPI()


@app.get("/")
async def root():
    print("Hello World")
    return {"message": "Hello World"}


@app.get("/zipcode/{zipcode}")
async def get_zipcode_details(zipcode: str):
    redis_client = redis.Redis(host='localhost', port=6379, db=0)
    data = redis_client.get(zipcode)
    print(data)
    if data:
        return data
    else:
        response = get(f"https://api.zippopotam.us/us/{zipcode}")
        data = response.json()
        redis_client.set(zipcode, str(data), 60)
        return data
