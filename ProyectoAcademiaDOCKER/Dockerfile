FROM python:3.11.6-alpine3.18

WORKDIR /app

RUN apk update \
    && apk add --no-cache gcc g++ musl postgresql-dev libffi-dev \
    && pip install --upgrade pip \
    && pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir numpy scipy pandas matplotlib
COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]