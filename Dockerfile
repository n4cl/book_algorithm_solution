FROM python:3.9.5-buster AS builder

ADD ./code /usr/local/code

ENTRYPOINT ["python", "/usr/local/code/exec.py"]
