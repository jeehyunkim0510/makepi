FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/jeehyunkim0510/makepi.git

WORKDIR /home/makepi/

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=django-insecure-fs^231tb14*0ah_4x24d$i290o3d2!ia=*61)q_5#+ycbfd-3j" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
