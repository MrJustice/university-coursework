FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

COPY . /usr/src/app
WORKDIR /usr/src/app

RUN pip install --upgrade pip
RUN pip -q install -r requirements/docker1.txt
RUN pip -q install -r requirements/docker2.txt 
RUN python3.8 manage.py collectstatic --no-input

# RUN ["chmod", "+x", "/usr/src/app/entrypoint.sh"]
# ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]
# CMD [ "python3.8", "manage.py", "runserver", "--insecure", "0.0.0.0:8000"] 