FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN pwd
RUN ls -al

EXPOSE 80

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]