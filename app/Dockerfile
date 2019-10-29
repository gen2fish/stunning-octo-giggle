FROM python:3.7

COPY . /app
WORKDIR /app
RUN ls -lart

RUN pip install -r requirements.txt
RUN chmod +x docker-entry.sh
EXPOSE 5000
CMD ["/bin/bash", "docker-entry.sh"]
