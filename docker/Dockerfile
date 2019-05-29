FROM python:3.7.3-alpine

COPY ./ /app

RUN apk --update add --no-cache git build-base mysql-client mariadb-dev && \
    pip --no-cache-dir install -r /app/requirements.txt

RUN chown -R nobody:nogroup /app
USER nobody
EXPOSE 8000
WORKDIR /app

HEALTHCHECK --interval=5m --timeout=3s \
  CMD curl -f http://localhost:8000/ || exit 1

CMD gunicorn --workers 3 --bind 0.0.0.0:8000 helpecBackend.wsgi --log-level INFO