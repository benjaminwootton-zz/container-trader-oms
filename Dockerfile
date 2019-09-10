FROM python

RUN pip install flask

ADD server.py /

EXPOSE 5000

CMD python3 /server.py

