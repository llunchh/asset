# 3.13.x 계열의 최신 패치를 자동 반영 (보안 업데이트 자동 흡수)
FROM python:3.11-slim

# 런타임 품질/로그 플러시
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# 작업 디렉토리 이동
WORKDIR /app

# 패키지 저장소의 목록을 최신 상태로 업데이트 + 빌드/PG 의존성 설치
# psycopg2/psycopg가 3.13에서 휠이 없으면 소스 빌드 → pg_config 필요
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      build-essential gcc libpq-dev pkg-config \
 && rm -rf /var/lib/apt/lists/*

# 비루트 사용자 생성
# 기본 python 이미지는 root로 동작 → 보안상 안전하지 않음.
# 운영 환경에서는 USER 지시어로 일반 사용자 전환해야 함.
RUN groupadd --system assetgroup && useradd --system --create-home --gid assetgroup assetuser

# 의존성 설치(루트 권한에서 시스템 레벨로 설치)
COPY --chown=assetuser:assetgroup requirements.txt .
<<<<<<< HEAD
RUN pip install --upgrade pip setuptools
RUN pip install --no-cache-dir -r requirements.txt
=======
RUN python -m pip install -U pip wheel \
 && pip install --no-cache-dir -r requirements.txt
>>>>>>> d1536bd (Update Dockerfile/requirements (Py3.13 + psycopg3))

# 소스 복사 (권한 소유자 변경)
COPY --chown=assetuser:assetgroup ./app /app

# 일반 계정으로 실행
USER assetuser

# 애플리케이션 기동 (uvicorn이 requirements에 있어야 함)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

