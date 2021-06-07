FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

COPY . /usr/src/app
WORKDIR /usr/src/app

VOLUME /media
VOLUME /common_static

RUN pip install --upgrade pip
RUN pip install -r requirements/docker1.txt
RUN pip install -r requirements/docker2.txt
RUN python3.8 manage.py collectstatic
CMD [ "python3.8", "manage.py", "runserver", "0.0.0.0:8000"] 