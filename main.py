import yfinance as yf
import json
from fastapi import FastAPI

app = FastAPI()


def get_stock_info(stock_name, period, type):
    dat = yf.Ticker(stock_name)
    history_prices = dat.history(period=period).get(type)
    num = history_prices.to_numpy()
    return num


def create_list_from_numpy(numpy_object):
    return [float(n) for n in numpy_object]


# Todays Price
@app.get("/{stock_name}")
def stock_price(stock_name):
    dat = yf.Ticker(stock_name)
    current_price = dat.analyst_price_targets["current"]
    return json.dumps({"Stock Price": current_price})


@app.get("/{stock_name}/{period}")
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
