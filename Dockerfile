FROM python:3.11
COPY requirements.txt .
RUN pip3 install -r /requirements.txt --no-cache-dir
COPY . .
CMD alembic upgrade head ; uvicorn app.main:app --host 0.0.0.0 --port 8000
