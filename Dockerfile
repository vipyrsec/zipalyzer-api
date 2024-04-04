FROM python:3.12-slim@sha256:5dc6f84b5e97bfb0c90abfb7c55f3cacc2cb6687c8f920b64a833a2219875997

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
