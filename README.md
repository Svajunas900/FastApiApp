## HOW TO SECTION:

Installing Application <br/>

Step 1. Navigate to directory where you want to clone application <br/>
   
Step 2. Clone repository using url https://github.com/Svajunas900/FastApiApp.git <br/>
````
git clone https://github.com/Svajunas900/FastApiApp.git
````
Step 3. Install all the dependencies
````
pip install fastapi[standard] yfinance sqlmodel
````

    
 ## Guide for starting this app locally
   
Step 1. Use this command 
````
fastapi dev main.py
````

## Guide for starting this app from docker <br/>

Step 1. Run this command in cmd:
````
docker build . -t appname
````
Step 2. Run:
````
docker run -p 3000:3000 appname 
````
## Guide for using this app <br/>

This app has three routes <br/> 

Route 1.  **/prices/{Stock_Symbols}** <br/>
Example   **/prices/msft** <br/>
Returns 
````
{"Stock Price": Current_Stock_Price}
````
Valid periods ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'] <br/>
Route 2.  **/prices/{stock_name}/{period}** <br/>
Example   **/prices/msft/5d** <br/>
Returns 
````
{"Stock Price": Current_Stock_Prices} <br/>
````
Valid periods ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'] <br/>
Route 3. **/volumes/{stock_name}/{period}** <br/>
Example  **/volumes/msft/1d** <br/>
Returns 
````
"{Stock_name-msft: {Stock_Volumes: [21697800.0, 18821000.0, 19144400.0, 18469500.0, 19110100.0], Stock_Average_of_5d: 19448560.0}}" <br/>
````

Route 4. **/check_db_full** <br/>
Returns 
````
{
    "av_7": 12.2,
    "time": "2024-12-11T14:27:02.957791",
    "stock": "msft",
    "av_21": 12.4,
    "month_price": 12.4,
    "id": 1,
    "price": 12,
    "av_14": 12.3,
    "daily_price": 12.2
}
````
Route 5. **/check_db_full/{time}** <br/>
Example **/check_db_full/1111999990** <br/>
Returns filtered list of json by time
````
 {
    "av_7": 418.478068850157,
    "time": "2024-12-11T16:56:15.099924",
    "stock": "msft",
    "av_21": 445.553685280411,
    "month_price": 311.837456446706,
    "id": 14,
    "price": 445.495,
    "av_14": 418.53026294244,
    "daily_price": 445.495
  },
  {
    "av_7": 418.478068850157,
    "time": "2024-12-11T16:58:08.374751",
    "stock": "msft",
    "av_21": 445.553685280411,
    "month_price": 425.2328951546,
    "id": 15,
    "price": 445.705,
    "av_14": 418.53026294244,
    "daily_price": 445.705
  }
````
Route for creating requests with post method <br/>
Route. **/requests** <br/>
Example **/requests** <br/>
Payload {"stock_name": "{STOCK_NAME}"} <br/>
Example {"stock_name": "msft"} <br/>

### Sonal cloud analysis url <br/>
**https://sonarcloud.io/project/overview?id=Svajunas900_FastApiApp** <br/>
**https://sonarcloud.io/summary/new_code?id=Svajunas900_FastApiApp&branch=main** <br/>

### Confluence <br/>
FastAPI stock app <br/>
https://svajunaskoncius.atlassian.net/l/cp/nsHBV8n1 <br/>
DB Investigation <br/>
https://svajunaskoncius.atlassian.net/l/cp/WzNqcTjL <br/>

## Examples of test cases
```
from fastapi.testclient import TestClient


def test_stock_prices(client: TestClient):
    response = client.get("/prices/msft")
    assert response.status_code == 200


def test_read_root(client: TestClient):
    response = client.get("/prices/msft/5d")
    assert response.status_code == 200
```
