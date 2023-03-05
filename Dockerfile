FROM python:3.11

WORKDIR /code

COPY . .

RUN pip install -r requirements.txt

EXPOSE 4000

CMD ["pyton3","manage.py","runserver","0.0.0.0:4000"]
