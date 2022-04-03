FROM python:3
RUN pip install flask
RUN pip install selenium
RUN pip install webdriver-manager
WORKDIR /app
COPY . /app/
CMD python3 main_scores.py
