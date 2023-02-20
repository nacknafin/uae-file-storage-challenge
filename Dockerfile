FROM python:3.10-slim-buster

RUN useradd worker --create-home
USER worker

WORKDIR /home/worker/app

ENV PATH "$PATH:/home/worker/.local/bin"

RUN pip install --user --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=worker:worker . .

CMD ["uvicorn", "app.main:app", "--host=0.0.0.0"]
