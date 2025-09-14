# Asset API Server

## ⚠️  **설명**
정보시스템 정보를 RESTful API로 제공하는 시스템

## 📀 Data 구조
1. 자산(Asset) 테이블
```sql
CREATE TABLE IF NOT EXISTS asset (
    id          UUID PRIMARY KEY,
    status      INTEGER NOT NULL,
    type        TEXT NOT NULL,
    category    INTEGER NOT NULL,
    subcategory INTEGER NOT NULL,
    os          INTEGER NOT NULL,
    hostname    VARCHAR(255) NOT NULL,
    ip          INET NOT NULL
);
```

2. 분류(Category) 테이블
```sql
CREATE TABLE category (
    code        SERIAL PRIMARY KEY,
    name        TEXT NOT NULL,
);
```

3. 세분류(SubCategory) 테이블
```sql
CREATE TABLE subcategory (
    code        SERIAL PRIMARY KEY,
    name        TEXT NOT NULL,
);
```

4. 운영체제(Os) 테이블
```sql
CREATE TABLE os (
    code        SERIAL PRIMARY KEY,
    name        TEXT NOT NULL,
)
```

## ⚙️ 실행
1. Repository clone 경로 이동
```bash
cd ~/dev/git
```
2. Repository clone
```bash
git clone https://github.com/llunchh/asset.git
```
3. Repository 경로 이동
```bash
cd asset
```
4. Docker compose 실행
```bash
docker-compose up -d
```
5. Docker Container 확인
```bash
docker ps

# asset_web, asset_db 컨테이너 확인
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
4. 분류(category)별 조회
```bash
http://192.168.6.53:8000/api/asset/all?category=server
http://192.168.6.53:8000/api/asset/all?category=network
http://192.168.6.53:8000/api/asset/all?category=security
```
5. 세분류(subcategory)별 조회
```bash
http://192.168.6.53:8000/api/asset/all?subcategory=firewall
http://192.168.6.53:8000/api/asset/all?subcategory=l3_switch
http://192.168.6.53:8000/api/asset/all?subcategory=app_server
```
6. 복합 조회
```bash
http://192.168.6.53:8000/api/asset/all?status=1&type=vm&category=server&subcategory=app_server
```
7. 응답 예시
```json
[
    {
        "id":"560d9440-47bb-4de8-8138-0add9acf6160",
        "status":1,
        "type":"vm",
        "category":"server",
        "subcategory":"app_server",
        "hostname":"ad-test",
        "ip":"192.168.6.108",
        "os":"windows"
    },
    {
        "id":"08f07553-60b9-4a69-99e4-31ee7b97337d",
        "status":1,
        "type":"pm",
        "category":"server",
        "subcategory":"sec_server",
        "hostname":"nasca&escort",
        "ip":"192.168.5.108",
        "os_name":"windows"
    }
]
```
