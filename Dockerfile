FROM python:3.8.2

COPY apis /api/apis
COPY Resource /api/Resource
COPY RssCrawler /api/RssCrawler
COPY config.py /api/config.py
COPY mainAPI.py /api/mainAPI.py
COPY r.txt /api/r.txt

WORKDIR /api
RUN pip install -r r.txt

CMD ["python", "mainAPI.py"]