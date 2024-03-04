# 기존의 Python 이미지를 사용합니다.
FROM python:3.10-slim

# 작업 디렉토리 설정
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 애플리케이션 파일들을 컨테이너로 복사
COPY . /usr/src/app/
# 필요한 패키지 설치
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]