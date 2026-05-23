from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Any

def success_response(

    code: str,

    message: str,

    data: Any,

    status_code: int = 200,

    ok: bool = True,
):

    content = {

        "statusCode": status_code,

        "ok": ok,

        "code": code,

        "message": message,

        "data": data
    }

    return JSONResponse(

        status_code=status_code,

        content=jsonable_encoder(content)
    )