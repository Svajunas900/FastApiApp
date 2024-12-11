import yfinance as yf


def get_stock_info(stock_name, period, type):
    dat = yf.Ticker(stock_name)
    history_prices = dat.history(period=period).get(type)
    num = history_prices.to_numpy()
    return num


def create_list_from_numpy(numpy_object):
    return [float(n) for n in numpy_object]