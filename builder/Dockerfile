# get python container
FROM python:3.9
WORKDIR /code
# get the requirements for the different pip modules needed
COPY ./requirements.txt /code/requirements.txt
# install the necessary modules
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
COPY ./data /code/app/data
# run the server on port 80 (HTTP)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

