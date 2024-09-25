FROM python:3.11-alpine as builder

WORKDIR /app

RUN apk add --no-cache gcc musl-dev python3-dev libffi-dev openssl-dev build-base cargo

RUN pip3 install poetry
COPY poetry.lock pyproject.toml /app/
RUN poetry config virtualenvs.in-project true && \
    poetry install --no-dev
RUN mv /app/.venv /.venv

FROM python:3.11-alpine
ENV PATH="/.venv/bin:$PATH"

COPY . /app
COPY --from=builder /.venv /.venv
WORKDIR /app
RUN rm Dockerfile && mv /app/init-script.sh /init-script.sh && chmod +x /init-script.sh
RUN adduser -DH -s /bin/false -u 1000 sekoia
USER sekoia

ENTRYPOINT ["/init-script.sh", "/.venv/bin/python", "main.py"]