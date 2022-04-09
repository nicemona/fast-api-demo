from typing import Dict

from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.v1 import router as v1_router
from utils.database import create_session
from utils.exception import NegativeValueException

app: FastAPI = FastAPI()

app.session_factory = create_session()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["OPTIONS", "GET", "POST"],
    allow_headers=[
        "accept",
        "Content-Type",
        "X-Requested-With",
    ],
)


@app.get("/", tags=["Index 🤖"])
async def index() -> Dict:
    return {"message": "This is FastAPI!"}


app.include_router(v1_router, prefix="/v1")


@app.exception_handler(NegativeValueException)
async def negative_value_exception_handler(
    request: Request, exception: NegativeValueException
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"message": exception.message},
    )
