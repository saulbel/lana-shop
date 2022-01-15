FROM python:3.8-slim-buster
WORKDIR /opt/lanashop
COPY requirements.txt /opt/lanashop/requirements.txt
RUN pip3 install -r requirements.txt
COPY . /opt/lanashop
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]