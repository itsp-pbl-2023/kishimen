FROM python:3.11

WORKDIR /workspace/kishimen/backend

ENV PIP_TARGET=/usr/local/pip-global
ENV PYTHONPATH=${PIP_TARGET}:${PYTHONPATH}
ENV PATH=${PIP_TARGET}/bin:${PATH}

COPY requirements.txt ./
RUN pip --disable-pip-version-check --no-cache-dir install -r requirements.txt \
  && rm -rf /tmp/pip-tmp

ENTRYPOINT ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]
