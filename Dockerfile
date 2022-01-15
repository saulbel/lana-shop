FROM python:3.8-slim-buster
RUN pip install --upgrade pip
RUN adduser -D lanauser
USER lanauser
WORKDIR /home/lanauser
COPY --chown=lanauser:lanauser requirements.txt requirements.txt
RUN pip install --lanauser -r requirements.txt
ENV PATH="/home/myuser/.local/bin:${PATH}"
COPY --chown=lanauser:lanauser . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]