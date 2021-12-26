FROM alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY start.py ./

RUN apk add py3-pip

RUN pip3 install -r requirements.txt

ENV FLASK_APP=start.py

# EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]