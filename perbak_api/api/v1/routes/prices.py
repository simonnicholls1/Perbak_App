from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from perbak_shared_library.data.database import get_db
from perbak_shared_library.data.models.price import Price
from perbak_api.services.oauth2 import get_current_user

router = APIRouter(
    prefix='/prices',
    tags=['Prices']
)

@router.get("/{symbol}")
def get_prices(symbol: str, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    prices = db.query(Price).filter(Price.symbol == symbol).all()
    if not prices:
        raise HTTPException(status_code=404, detail="Item not found")
    return prices