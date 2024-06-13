FROM python:3.11.9-bullseye

RUN apt-get update && apt-get install -y \
    git \
    libhdf5-dev

WORKDIR /usr/src/app

RUN git clone https://github.com/xian-network/xian-contracting.git
RUN pip install pytest
RUN pip install ./xian-contracting/
RUN pip install xian-py

CMD ["tail", "-f", "/dev/null"]