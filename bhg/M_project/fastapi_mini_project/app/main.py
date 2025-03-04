from fastapi import FastAPI
from pydantic import BaseModel
from app.core.config import settings

app = FastAPI()

# 응답 모델 정의
class RootResponse(BaseModel):
    message: str
    debug: bool

@app.get("/", response_model=RootResponse)
def read_root():
    return {"message": "FastAPI 프로젝트가 시작되었습니다!", "debug": settings.DEBUG}