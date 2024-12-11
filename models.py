from sqlmodel import Field, SQLModel
from datetime import datetime 

class Requests(SQLModel, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)
    time: datetime = Field(default=datetime.now())
    stock: str 
    price: int 
    av_7: float 
    av_14: float
    av_21: float
    daily_price: float
    month_price: float
