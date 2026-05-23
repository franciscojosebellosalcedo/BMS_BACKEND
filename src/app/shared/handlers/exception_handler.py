from fastapi import Request
from fastapi.responses import JSONResponse

from app.shared.exceptions.app_exception import AppException

async def exception_handler(
    request: Request,
    exception: AppException
    
):
    return JSONResponse(
        status_code= exception.status_code,
        content= {
            "data": None,
            "ok": False,
            "code": exception.code,
            "status_code": exception.status_code,
            "message": exception.message
        }
    )