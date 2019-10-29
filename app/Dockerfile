FROM python:3.7

COPY . /app
WORKDIR /app
RUN ls -lart

RUN pip install -r requirements.txt
RUN python --version
ENTRYPOINT ["python"]
CMD ["run.py"]
