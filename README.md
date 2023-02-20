# uae-file-storage-challenge
UA energy file storage challenge solution

Author: Onanko Anastasiia

This repository contains an API for a file storage service that allows users to upload, download, and manage files.

Implement the following endpoints:
    -- POST /files for uploading files
    -- GET /files/{id} for downloading files
    -- GET /files for listing all the uploaded files
    -- HEAD /files/{id} for getting information about files (without downloading)
Ability to save and download files with Cyrillic characters

## Prerequisites

- [pip](https://pip.pypa.io)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/) `2023-02-16` or later
- [Python](https://www.python.org/) `3.10` or higher
- [Docker](https://docs.docker.com/compose/)
- [docker-compose](https://docs.docker.com/compose/)

## Installing

You have to options (may install both):
- Install Virtualenv
- Install docker & docker-compose, and run `docker-compose build` to build an image with setted up environtent.

## Using

Whole app is implemented as backend app.
Open file `settings.py` and set the directory where you want to save files.
To run the app use one of the next command from repository dir(depend on what you have installed).

To run app in virtual env:
1. Create a virtual environment by running the following command:
```
python3.10 -m venv uae-test
```
2. Activate the virtual environment:
```
# for Windows:
venv\Scripts\activate.bat

# for Linux or macOS:
source venv/bin/activate
```
3. Install the project dependencies by running:
```
pip install -r requirements.txt
```
4. Start the API server by running:

```
uvicorn --reload app.main:app

#if port 8000 is occupied you can put another
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

To run app in docker contained:
0. Start Docker on your computer
1. Build the Docker image by running the following command:
```
docker build -t uae-file-storage
```
2. Start the Docker container by running:
```
docker-compose up
```
It will run the app on 8000 port (you may change it by setting `LOCAL_WEB_PORT` environment parameter)

To get into app UI follow `http://localhost:8000/docs` link in your browser to upload files and get info about them

To run tests `python3.10 -m pytest tests/test_files.py`
