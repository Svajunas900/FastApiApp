from fastapi import HTTPException


class ExceptionHandler:
    def status_code_404():
        return HTTPException(status_code=404, detail={"status": 404, "description": "Requested route doesn't exist", "solution": "Check valid routes in the documentation https://github.com/Svajunas900/FastApiApp"})
    
    def status_code_400():
        return HTTPException(status_code=400, detail={"status": 400, "description": "Stock name doesn't exist ", "solution": "Check stock name symbols"})