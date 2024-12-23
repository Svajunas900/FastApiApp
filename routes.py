import yfinance as yf
import json
from fastapi import Depends, Query, APIRouter
from sqlmodel import Session, select
from typing import Annotated
from models import Requests
from functions import get_stock_info, create_list_from_numpy
from DbConnection import SQLDbConnection
from datetime import datetime
from ExceptionHandler import ExceptionHandler


sql_connection = SQLDbConnection()


def get_session():
    with Session(sql_connection) as session:
        yield session 


SessionDep = Annotated[Session, Depends(get_session)]
router = APIRouter()


@router.get("/prices/{stock_name}", tags=["stocks"])
def stock_price(stock_name: str):
    dat = yf.Ticker(stock_name)  
    try:
        current_price = dat.analyst_price_targets["current"]
    except:
        raise ExceptionHandler.status_code_400()
    return json.dumps({"Stock Price": current_price})


@router.get("/prices/{stock_name}/{period}", tags=["stocks"])
def read_root(stock_name: str, period: str):
    numpy_open_prices = get_stock_info(stock_name, period, "Open")
    prices_list = create_list_from_numpy(numpy_open_prices)
    return json.dumps({"Stock Prices" : prices_list})


@router.get("/volumes/{stock_name}/{period}", tags=["stocks"])
def volumes_and_averages(stock_name: str, period: str):
    numpy_volumes = get_stock_info(stock_name, period, "Volume")
    volumes_list = create_list_from_numpy(numpy_volumes)
    average = []
    if volumes_list:
        average = sum(volumes_list) / len(volumes_list)
    return json.dumps({f"Stock_name-{stock_name}":
                       {"Stock_Volumes":volumes_list , f"Stock_Average_of_{period}":average}})


@router.post("/requests", tags=["stocks"])
def create_request(request: Requests, session: SessionDep):
    dat = yf.Ticker(request.stock)
    try:
        current_price = dat.analyst_price_targets["current"]
    except:
        raise ExceptionHandler.status_code_400()
    numpy_open_prices = get_stock_info(request.stock, "1mo", "Open")
    prices_list = create_list_from_numpy(numpy_open_prices)
    total, av_7, av_14, av_21 = 0, 0, 0, 0
    av_30 = total / len(prices_list)
    time = datetime.now()
    for i in range(len(prices_list)):
        total += prices_list[i]
        if i == 6:
            av_7 = total / 7
        if i == 13:
            av_14 = total / 14
        if i == 20:
            av_21 = total / 20

    request = Requests(time=time, stock=request.stock, price=current_price, av_7=av_7, 
                   av_14=av_14, av_21=av_21, daily_price=current_price, 
                   month_price=av_30)
    session.add(request)
    session.commit()
    session.refresh(request)
    return request


@router.get("/check_db_full", tags=["stocks"])
def read_request(session: SessionDep, offset: int=0, limit: Annotated[int, Query(le=100)] = 100,):
    requests = session.exec(select(Requests).offset(offset).limit(limit)).all()
    return requests


# example url http://127.0.0.1:8000/check_db_full/1111999990
@router.get("/check_db_full/{user_time}", tags=["stocks"])
def read_request_on_time(user_time: str, session: SessionDep, offset: int=0, 
                         limit: Annotated[int, Query(le=100)] = 100):
    requests = session.exec(select(Requests).offset(offset).limit(limit)).all()
    result = []
    for request in requests:
        time = datetime.fromtimestamp(int(user_time))
        if time < request.time:
            result.append(request)
    return result


class Facade:
    def __init__(self, stock_name, period):
        self.prices = read_root(stock_name, period)
        self.volumes = volumes_and_averages(stock_name, period)
    
    def __str__(self):
        return {self.prices, self.volumes}
    

@router.get("/pricesAndVolumes/{stock_name}/{period}", tags=["stocks"])
def prices_and_volumes(stock_name: str, period: str):
    return Facade(stock_name, period)


