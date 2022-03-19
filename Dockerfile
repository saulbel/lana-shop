FROM python:3.8-slim-buster
WORKDIR /opt/shop
COPY requirements.txt /opt/shop/requirements.txt
RUN pip3 install -r requirements.txt
COPY . /opt/shop
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
