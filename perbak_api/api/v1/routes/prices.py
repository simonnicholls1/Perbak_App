from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from etl_service.database import get_db
from etl_service.models.price import Price

router = APIRouter(
    prefix='/prices',
    tags=['Prices']
)

@router.get("/{symbol}")
def get_prices(symbol: str, db: Session = Depends(get_db)):
    prices = db.query(Price).filter(Price.symbol == symbol).all()
    if not prices:
        raise HTTPException(status_code=404, detail="Item not found")
    return prices