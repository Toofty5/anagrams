FROM python:3.9-slim-bullseye
WORKDIR /app
RUN pip3 install flask
COPY . /app
ENV FLASK_APP=/app/codetest.py
EXPOSE 5000
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]