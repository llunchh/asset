# Asset API Server

## ⚠️  **설명**
정보시스템 정보를 RESTful API로 제공하는 시스템

## 📀 Data 구조
1. Asset 테이블
```sql
CREATE TABLE IF NOT EXISTS asset (
    id          TEXT PRIMARY KEY,
    status      INTEGER NOT NULL,
    type        TEXT NOT NULL,
    category    TEXT NOT NULL,
    os          INTEGER NOT NULL,
    hostname    TEXT NOT NULL,
    ip          TEXT NOT NULL
);
```
2. Os 테이블
```sql
CREATE TABLE os (
    code        INTEGER NOT NULL,
    name        TEXT NOT NULL,
    PRIMARY     KEY(code AUTOINCREMENT)
)
```

## ⚙️  Installation

1. 가상환경(venv) 생성
```bash
python3 -m venv asset
```
2. 가상환경 경로 진입
```bash
cd asset
```
3. 가상환경 활성화
```bash
source bin/activate
```
4. git 경로 이동
```bash
cd ~/dev/git
```
5. Repository clone
```bash
git clone git@github.com:rracle/asset.git
```
6. 파이썬 패키지 설치
```bash
pip3 install -r requirements.txt
```
7. 실행
```bash
uvicorn main:app --reload
```
## ✅ 사용 예시
1. 전체 자산(asset) 조회
```bash
http://192.168.6.53:8000/api/asset/all
```
2. 활성화별 조회
```bash
http://192.168.6.53:8000/api/asset/all?status=1
http://192.168.6.53:8000/api/asset/all?status=0
```
3. 타입(type)별 조회
```bash
http://192.168.6.53:8000/api/asset/all?type=vm
http://192.168.6.53:8000/api/asset/all?type=pm
```
4. 카테고리별 조회
```bash
http://192.168.6.53:8000/api/asset/all?category=server
http://192.168.6.53:8000/api/asset/all?category=network
http://192.168.6.53:8000/api/asset/all?category=security
```
5. 복합 조회
```bash
http://192.168.6.53:8000/api/asset/all?status=1&type=vm&category=server
```
