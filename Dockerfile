# 3.11.x 계열의 최신 패치를 자동 반영 (보안 업데이트 자동 흡수)
FROM python:3.11-slim

# 작업 디렉토리 이동
WORKDIR /app

# 패키지 저장소의 목록을 최신 상태로 업데이트 및 불필요 패키지 삭제
RUN apt-get update \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


# 비루트 사용자 생성
# 기본 python 이미지는 root로 동작 → 보안상 안전하지 않음.
# 운영 환경에서는 USER 지시어로 일반 사용자 전환해야 함.
RUN groupadd --system assetgroup && useradd --system --create-home --gid assetgroup assetuser

# uv 설치
# --no-cache-dir : pip 캐시 남기지 않음
# --upgrade : 최신 uv 설치(재현성이 필요한 경우 버젼 명시 필요)
RUN pip install --no-cache-dir --upgrade uv

# 의존성 설치(루트 권한에서 시스템 레벨로 설치)
COPY --chown=assetuser:assetgroup pyproject.toml uv.lock .

# uv 기반으로 패키지 설치
# --system: 시스템 전역에 설치 (가상환경 .venv 안만듦)
# --no-cache: 빌드 캐시 최소화
# --no-dev: 개발용 의존성 제외
RUN uv sync --system --no-cache --no-dev

# 소스 복사 (권한 소유자 변경)
COPY --chown=assetuser:assetgroup ./app /app

# 일반 계정으로 실행
USER assetuser

# 애플리케이션 기동 (uvicorn이 pyproject.toml 의 dependencies 안에 있어야 함)
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

