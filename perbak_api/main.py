from fastapi import FastAPI, HTTPException
from perbak_api.api.v1.routes import prices
import uvicorn
from perbak_api.data.models import Base

app = FastAPI()

app.include_router(prices.router)

@app.on_event("startup")
async def startup():
    #Base.metadata.create_all(bind=engine)
    pass

@app.on_event("shutdown")
async def shutdown():
    pass
    #await get_db().close_all()

if __name__ =='__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)