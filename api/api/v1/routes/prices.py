from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from api.data.models import Price
from api.data.database import get_db

app = FastAPI()

@app.get("/prices/{isin}")
def get_prices(isin: str, db: Session = Depends(get_db)):
    prices = db.query(Price).filter(Price.isin == isin).all()
    if not prices:
        raise HTTPException(status_code=404, detail="Item not found")
    return prices