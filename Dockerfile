FROM python:3.9-buster
COPY  ./api /usr/local/app
WORKDIR /usr/local/app
RUN pip install -r /usr/local/app/requiriments.txt
EXPOSE 8000
#cmd ["python","manage.py", "runserver",  "0.0.0.0:8000"]


#RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
#COPY nginx.default /etc/nginx/sites-available/default
#RUN ln -sf /dev/stdout /var/log/nginx/access.log \
#    && ln -sf /dev/stderr /var/log/nginx/error.log
