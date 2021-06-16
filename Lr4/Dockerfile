FROM python:3.8

RUN pip3 install python-telegram-bot schedule Flask Flask-Migrate Flask-MySQL Flask-SQLAlchemy youtube-dl aiogram
WORKDIR .
COPY . .
ENTRYPOINT ["python"]
CMD ["main.py"]
