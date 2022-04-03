FROM moditamam/selenium:python3
RUN pip install flask
RUN pip install selenium
WORKDIR /app
COPY . /app/
RUN pip install webdriver-manager
CMD python3 main_scores.py
