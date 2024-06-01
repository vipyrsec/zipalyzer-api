FROM python:3.12-slim@sha256:afc139a0a640942491ec481ad8dda10f2c5b753f5c969393b12480155fe15a63

# Define Git SHA build argument for sentry
ARG git_sha="development"
ENV GIT_SHA=$git_sha

WORKDIR /home/zipalyzer

COPY requirements/requirements.txt .
RUN python -m pip install --requirement requirements.txt

COPY pyproject.toml pyproject.toml
COPY src/ src/
RUN python -m pip install .

RUN adduser --disabled-password zipalyzer
USER zipalyzer

# HTTP
EXPOSE 8080

CMD ["uvicorn", "zipalyzer.server:app", "--host", "0.0.0.0", "--port", "8080"]
