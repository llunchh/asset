from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers import api_router

app = FastAPI(
    title="Asset API",
    description="Asset documentation",
    version="1.0.0",
)

# CORS 허용할 도메인 목록
origins = [
    "https://example.com",
    "https://asset.emro.co.kr",
    "http://localhost:8000"
]

# CORS 미들웨어 등록
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # 특정 도메인만 허용
    allow_credentials=True,         # 쿠키 포함 허용 여부
    allow_methods=["GET"],            # 허용할 메서드 (GET, POST, PUT, DELETE 등)
    allow_headers=["Authorization", "Content-Type"],            # 허용할 요청 헤더
)

app.include_router(api_router, prefix="/api")
