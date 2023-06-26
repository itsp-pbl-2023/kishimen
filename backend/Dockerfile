FROM python:3.11

WORKDIR /workspace/kishimen/backend

COPY requirements.txt ./
RUN --mount=type=cache,mode=0755,target=/root/.cache/pip pip --disable-pip-version-check install -r requirements.txt \
  && rm -rf /tmp/pip-tmp

ENTRYPOINT ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]
