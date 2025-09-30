# 3.13.x 계열의 최신 패치를 자동 반영 (보안 업데이트 자동 흡수)
FROM python:3.11-slim

# 작업 디렉토리 이동
WORKDIR /app

# 패키지 저장소의 목록을 최신 상태로 업데이트
RUN apt-get update

# 비루트 사용자 생성
# 기본 python 이미지는 root로 동작 → 보안상 안전하지 않음.
# 운영 환경에서는 USER 지시어로 일반 사용자 전환해야 함.
RUN groupadd --system assetgroup && useradd --system --create-home --gid assetgroup assetuser

# 복사 전 권한 준비
COPY --chown=assetuser:assetgroup requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 소스 복사 (권한 소유자 변경)
COPY --chown=assetuser:assetgroup ./app /app

# 일반 계정으로 실행
USER assetuser

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
