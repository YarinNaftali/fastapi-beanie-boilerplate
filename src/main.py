from fastapi import FastAPI  # Import FastAPI
from api.v1.router import router as v1_router  # Import v1 router
from database.database import init_beanie  # Import init_beanie

app = FastAPI()

app.include_router(v1_router)  # Include v1 router

@app.on_event("startup")
async def startup_event():
    '''This function will be called when the app starts up.'''
    await init_beanie()


@app.get("/")
async def root():
    return {"message": "Spread the love!"}
