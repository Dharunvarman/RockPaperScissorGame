FROM python:3
 
WORKDIR /dev_local

COPY requirements.txt /dev_local/requirements.txt

COPY sample.py /sample.py

RUN pip install -r /dev_local/requirements.txt
 
COPY entry.sh /entry.sh
RUN chmod 744 /entry.sh

# ENTRYPOINT ["python"]
# CMD ["/sample.py"]