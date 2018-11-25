FROM python:3.4-alpine
COPY . /app
WORKDIR /app
RUN apk add --no-cache gcc musl-dev
RUN pip install -r requirements.txt
CMD gunicorn app:app --workers=2 --bind=0.0.0.0:5000 --pid=pid --worker-class=meinheld.gmeinheld.MeinheldWorker
