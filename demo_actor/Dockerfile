FROM python:3.10-slim

WORKDIR /code
COPY requirements.txt /code/requirements.txt

RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . /code/app


CMD ["python", "/code/app/demo_actor_service.py"]