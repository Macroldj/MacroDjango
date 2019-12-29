FROM python:3.7-alpine3.10
MAINTAINER macroldj Alan Li

WORKDIR /home/workspace

COPY . . 

ADD ./requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir  -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com -r /tmp/requirements.txt && rm -rf /tmp/requirements.txt
CMD ["sh","macroDemo/runserver.sh"]
