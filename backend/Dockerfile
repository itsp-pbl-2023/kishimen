FROM python:3.7

WORKDIR /workspace/kishimen/backend

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]
