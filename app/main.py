from typing import Optional
from fastapi import FastAPI
import redis

 ## REQUIRED FOR REMOTE DEBUGGING
import debugpy
debugpy.listen(("0.0.0.0", 5678))
# debugpy.wait_for_client() # Optional

app = FastAPI()
r = redis.Redis(host="redis", port=6379)

@app.get("/")
def read_root():
    return {"Hello": "World /hits"}

@app.get("/hits")
def read_root():
    r.incr("hits")
    return {"number of ": r.get("hits")}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}