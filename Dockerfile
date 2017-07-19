from ubuntu:latest

COPY ./requirements.txt /tmp

RUN apt-get -y update && apt-get install -y \
    python3 \
    python3-pip

RUN pip3 install -r /tmp/requirements.txt

CMD /bin/bash
    
	
