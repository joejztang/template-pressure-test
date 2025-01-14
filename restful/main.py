import asyncio
import os
import random

from fastapi import FastAPI

app = FastAPI()


@app.get("/foobar")
async def foobar():
    delayed = random.randint(1, 3)
    pid = os.getpid()
    await asyncio.sleep(delayed)
    return {"message": f"delayed reply from {pid} after {delayed} seconds", "pid": pid}


@app.get("/foobar-sync")
def foobar_sync():
    delayed = random.randint(1, 3)
    pid = os.getpid()
    return {"message": f"delayed reply from {pid} after {delayed} seconds", "pid": pid}
