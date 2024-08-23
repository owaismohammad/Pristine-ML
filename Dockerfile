FROM python:3.12.3

WORKDIR /modelPristine

COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx libgl1-mesa-dev libglu1-mesa && \
    rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt

COPY . .
CMD [ "python", "app.py" ] 

