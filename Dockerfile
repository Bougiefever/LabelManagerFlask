FROM ubuntu:16.04

# apt-get and system utilities
RUN apt-get update && apt-get install -y \
    curl apt-utils apt-transport-https debconf-utils gcc build-essential g++-5\
    && rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install gettext nano vim -y

# install python and pip3
RUN apt-get install -y python3-pip python3-dev

# adding custom MS repository
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-release.list

# install SQL Server drivers
RUN apt-get update && ACCEPT_EULA=Y apt-get -y install msodbcsql17
RUN apt-get -y install unixodbc unixodbc-dev


# upgrade pip
RUN pip3 install --upgrade pip

# install necessary locales
RUN apt-get update && apt-get install -y locales \
    && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \
    && locale-gen

ENV FLASK_CONFIG=prod
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD [ "gunicorn", "-b", "0.0.0.0:8000", "app"]