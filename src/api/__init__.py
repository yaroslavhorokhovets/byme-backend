from functools import wraps

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from config import root_path
from src.common.exception import InputParamError, CustomError, Unauthorized, ConflictMessage

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI(title="ApiByMe", root_path=root_path)

def build_message_susccess(data=None, page=None):
    result = {"message": "request successful", "code": 200}
    if isinstance(data, dict):
        result.update(data)
    else:
        result["data"] = data
    if page:
        result["page"] = page
    return result


@app.exception_handler(InputParamError)
async def input_param_error(request: Request, exc: InputParamError):
    return JSONResponse(
        status_code=401,
        content={
            "code": 401,
            "message": exc.message
        },
    )


@app.exception_handler(ConflictMessage)
async def conflict_error(request: Request, exc: ConflictMessage):
    return JSONResponse(
        status_code=409,
        content={
            "code": 409,
            "message": exc.message
        },
    )


@app.exception_handler(CustomError)
async def custom_error(request: Request, exc: CustomError):
    return  JSONResponse(
        status_code=401,
        content={
            "code": 401,
            "message": exc.message
        },
    )


@app.exception_handler(Unauthorized)
async def unauthorized(request: Request, exc: Unauthorized):
    return JSONResponse(
        status_code=412,
        content={
            "code": 412,
            "message": exc.message
        },
    )


def try_except_response(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return JSONResponse(status_code=200, content=func(*args, **kwargs))
        except InputParamError as ip:
            return input_param_error()
        except CustomError as ce:
            return custom_error()
        except ConflictMessage as ce:
            return conflict_error()
        except Exception as ex:
            return 500, 500

    return wrapper
