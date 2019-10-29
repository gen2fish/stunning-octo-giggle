FROM python:3.7

COPY . /app
WORKDIR /app
RUN ls -lart

RUN pip install -r requirements.txt
RUN python --version
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "run"]
