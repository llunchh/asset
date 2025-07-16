# Asset API Server

## ⚠️  **설명**
정보시스템 정보를 RESTful API로 제공하는 시스템

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
