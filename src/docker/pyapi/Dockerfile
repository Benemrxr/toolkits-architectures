FROM python:3.8-slim-buster

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Tell flask which file to use as entrypoint
ENV FLASK_APP=/src/main.py

# Install pip requirements
ADD /src/requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
ADD /src /app

# Switching to a non-root user
RUN useradd appuser && chown -R appuser /app

# Changing owner of data directory
RUN mkdir /data
RUN chown -R appuser /data

USER appuser

CMD ["python", "main.py"]
