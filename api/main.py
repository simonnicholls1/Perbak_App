from fastapi import FastAPI, HTTPException
from api.api.v1.routes import prices
import uvicorn
from api.data.models import Base
from api.data.database import SessionLocal

app = FastAPI()

app.include_router(prices.router)

@app.on_event("startup")
async def startup():
    #Base.metadata.create_all(bind=engine)
    pass

@app.on_event("shutdown")
async def shutdown():
    await SessionLocal.close_all()

if __name__ =='__main__':
    uvicorn.run(app, host="0.0.0.0", port=8900)