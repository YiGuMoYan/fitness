FROM python:3.7-slim

LABEL authors="YiGuMoYan"

RUN apt-get update && apt-get install -y git

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN python -m pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "start_tasks"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
