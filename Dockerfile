FROM python:3.9-slim
WORKDIR /pythontest
COPY test-peer-1.py /pythontest/test-peer-1.py
COPY test-peer-2.py /pythontest/test-peer-2.py
EXPOSE 8001
EXPOSE 8002