FROM python:3.12.0
RUN python -m pip install django
COPY . code
WORKDIR /code
EXPOSE 8000
ENTRYPOINT ["python", "mysite/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]