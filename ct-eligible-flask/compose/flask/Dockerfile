FROM python:3.6.1

ENV PYTHONUNBUFFERED 1

RUN groupadd -r flask && \
    useradd -r -g flask flask

EXPOSE 4000

RUN mkdir /ct_eligible

COPY ./app /ct_eligible/app
COPY ./data /ct_eligible/data
COPY index.py ct_eligible/index.py
COPY requirements.txt ct_eligible/requirements.txt

COPY ./compose/flask/entrypoint.sh entrypoint.sh
RUN chmod +x entrypoint.sh

RUN pip3 install \
    -r ct_eligible/requirements.txt \
    --no-cache-dir

ENV MONGO_URI mongodb://mongodb:27017/ct-eligible

ENTRYPOINT ["./entrypoint.sh"]
