FROM python:3

RUN apt update

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

COPY scrapper.py ./

CMD [ "python3", "./scrapper.py"]



#FROM python:3.8-slim-buster
#
#WORKDIR /app
#
#COPY requirements.txt requirements.txt
#RUN pip3 install -r requirements.txt
#
#COPY . .
#
#CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]