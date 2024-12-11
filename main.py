import yfinance as yf
import json
from fastapi import FastAPI, Depends, FastAPI, Query
from sqlmodel import Session, create_engine, SQLModel, select
from typing import Annotated
from models import Requests
from functions import get_stock_info, create_list_from_numpy
from contextlib import asynccontextmanager
from DbConnection import SQLDbConnection


@asynccontextmanager
async def lifespan(app):
    create_db_and_tables()
    yield

sql_connection = SQLDbConnection()

def get_session():
    with Session(sql_connection) as session:
        yield session 


def create_db_and_tables():
    SQLModel.metadata.create_all(sql_connection)


app = FastAPI(lifespan=lifespan)
SessionDep = Annotated[Session, Depends(get_session)]


@app.get("/price/{stock_name}")
def stock_price(stock_name):
    dat = yf.Ticker(stock_name)
    current_price = dat.analyst_price_targets["current"]
    return json.dumps({"Stock Price": current_price})


@app.get("prices/{stock_name}/{period}")
def read_root(stock_name, period):
    numpy_open_prices = get_stock_info(stock_name, period, "Open")
    prices_list = create_list_from_numpy(numpy_open_prices)
    return json.dumps({"Stock Prices" : prices_list})


@app.get("/volumes/{stock_name}/{period}")
def volumes_and_averages(stock_name, period):
    numpy_volumes = get_stock_info(stock_name, period, "Volume")
    volumes_list = create_list_from_numpy(numpy_volumes)
    average = sum(volumes_list) / len(volumes_list)
    return json.dumps({f"Stock_name-{stock_name}":{"Stock_Volumes":volumes_list , f"Stock_Average_of_{period}":average}})


@app.post("/requests")
def create_request(request: Requests, session: SessionDep):
    request = Requests(time=request.time, stock=request.stock, price=request.price, av_7=request.av_7, 
                   av_14=request.av_14, av_21=request.av_21, daily_price=request.daily_price, 
                   month_price=request.month_price)
    session.add(request)
    session.commit()
    session.refresh(request)
    return request


@app.get("/check_db_full")
def read_request(session: SessionDep, offset: int=0, limit: Annotated[int, Query(le=100)] = 100,):
    requests = session.exec(select(Requests).offset(offset).limit(limit)).all()
    return requests

@app.get("/check_db_full/{time}")
def re():
    return
