FROM python:3.7.10
WORKDIR /meusvideos-backend
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . .
RUN python manage.py makemigrations && python manage.py migrate
EXPOSE 8000
CMD ["python","manage.py","runserver"]