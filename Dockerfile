from python:3.11
copy . /app
workdir /app
run pip install -r requirements.txt
expose $port
cmd gunicorn --workers=4 --bind 0.0.0.0:$port app:app