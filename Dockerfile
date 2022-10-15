From pyhton:3.9
copy . /app
workdir /app
run pip install -r requirements.txt
expose $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app

