## Guide for start this app

Step 1. Run this command in cmd: docker build . -t appname

Step 2. Run: docker run -p 3000:3000 appname

## Guide for using this app

This app has three routes 

Route 1. /{Stock_Symbols}
Example /msft
Returns {"Stock Price": Current_Stock_Price}

Valid periods ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
Route 2. /{stock_name}/{period}
Example /msft/5d
Returns {"Stock Price": Current_Stock_Price}

Valid periods ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
Route 3. /values/{stock_name}/{period}
Example /values/msft/1d
Returns {"Stock Price": Current_Stock_Price}


