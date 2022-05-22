# 
FROM python:3.9 AS APIdevelopment

# 
WORKDIR /numerapp/src/app

# 
COPY ./requirements.txt /numerapp/src/app/requirements.txt

RUN pip install --upgrade pip
# 
RUN pip install --no-cache-dir --upgrade -r /numerapp/src/app/requirements.txt

# 
COPY . /numerapp/src/app

EXPOSE 3000

