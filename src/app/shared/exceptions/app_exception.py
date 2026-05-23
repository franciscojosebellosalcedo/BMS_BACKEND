
class AppException (Exception):
    
    def __init__(
        self,
        code: str,
        message: str,
        ok: bool = False,
        status_code: int = 400,
    ):
        self.code = code
        self.ok = ok
        self.data = None
        self.message = message
        self.status_code = status_code