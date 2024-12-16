import yfinance as yf
from DbConnection import SQLDbConnection
from sqlmodel import SQLModel
from contextlib import asynccontextmanager


sql_connection = SQLDbConnection()


def get_stock_info(stock_name, period, type):
    dat = yf.Ticker(stock_name)
    history_prices = dat.history(period=period).get(type)
    num = history_prices.to_numpy()
    return num


def create_list_from_numpy(numpy_object):
    return [float(n) for n in numpy_object]


@asynccontextmanager
async def lifespan(app):
    create_db_and_tables()
    yield


def create_db_and_tables():
    SQLModel.metadata.create_all(sql_connection)