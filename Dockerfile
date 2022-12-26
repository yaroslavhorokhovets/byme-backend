FROM python:3.8

WORKDIR /home/projects/byme

ADD ./ /home/projects/byme

RUN pip install -r requirement.txt

ENV VM_TYPE=TEST\
    BYME_HOME=/home/projects/byme

WORKDIR $BYME_HOME
EXPOSE 8080

CMD ["uvicorn", "start_app:app", "--host", "0.0.0.0", "--port", "8080"]
