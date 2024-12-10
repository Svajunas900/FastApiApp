## Guide for starting this app <br/>

Step 1. Run this command in cmd:  **docker build . -t appname** <br/>

Step 2. Run:  **docker run -p 3000:3000 appname** <br/>

## Guide for using this app <br/>

This app has three routes <br/> 

Route 1.  /{Stock_Symbols} <br/>
Example   /msft <br/>
Returns {"Stock Price": Current_Stock_Price} <br/>

Valid periods ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'] <br/>
Route 2.  /{stock_name}/{period} <br/>
Example   /msft/5d <br/>
Returns {"Stock Price": Current_Stock_Price} <br/>

Valid periods ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'] <br/>
Route 3. /values/{stock_name}/{period} <br/>
Example  /values/msft/1d <br/>
Returns {"Stock Price": Current_Stock_Price} <br/>


