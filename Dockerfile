FROM python:3.9-buster
COPY  ./api /usr/local/app
WORKDIR /usr/local/app
RUN pip install -r /usr/local/app/requiriments.txt
RUN apt-get install libpq-dev && pip3 install psycopg2-binary
RUN find './' -path "*/migrations/*.py*" -not -name "__init__.pyc*" -delete
EXPOSE 8000
#cmd ["python","manage.py", "runserver",  "0.0.0.0:8000"]


#RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
#COPY nginx.default /etc/nginx/sites-available/default
#RUN ln -sf /dev/stdout /var/log/nginx/access.log \
#    && ln -sf /dev/stderr /var/log/nginx/error.log
