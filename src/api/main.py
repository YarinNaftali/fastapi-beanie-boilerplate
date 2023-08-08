from fastapi import FastAPI # Import FastAPI
from api.v1.router import router as v1_router # Import v1 router

app = FastAPI()

app.include_router(v1_router) # Include v1 router

@app.get("/")
async def root():
    return {"message": "Spread the love!"}


