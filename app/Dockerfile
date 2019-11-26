FROM python:3.7

RUN mkdir /app
WORKDIR /app
RUN ls -lart

ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY . /app
RUN chmod +x docker-entry.sh
EXPOSE 5000
CMD ["/bin/bash", "docker-entry.sh"]
