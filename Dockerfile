# start by pulling the python image
FROM ubuntu:20.04


ENV TZ=Europe/Kiev
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app


# install the dependencies and packages in the requirements file
RUN apt-get update -y && apt-get install -y python3-pip build-essential libssl-dev libffi-dev python3-dev
RUN apt-get install -y cmake
RUN pip3 install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT [ "python3" ]

CMD ["app.py" ]
