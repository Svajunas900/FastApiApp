from fastapi import  FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from routes import router
from functions import lifespan


app = FastAPI(lifespan=lifespan)


@app.exception_handler(500)
async def internal_exception_handler(request: Request, exc: Exception):
  return JSONResponse(status_code=500, 
                      content=jsonable_encoder(
    {"status": 500, 
     "description": "Invalid request format or naming", 
     "solution": "Check post request format and naming"})
     )


# example url http://127.0.0.1:8000/check_db_full/1111999990

app.include_router(router)