# use a small base image
FROM python:3.11-slim


# set working directory
WORKDIR /app


# install build deps and pip
RUN apt-get update && apt-get install -y --no-install-recommends \
build-essential \
&& rm -rf /var/lib/apt/lists/*


# copy requirements first to leverage caching
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


# copy app
COPY . /app


# expose port
EXPOSE 5000


# use gunicorn for production-like server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]