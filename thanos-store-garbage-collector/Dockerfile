FROM  --platform=linux/amd64 python:3.12-alpine

WORKDIR /home

# Copy app artifacts
COPY thanos-store-garbage-collector.py thanos-store-garbage-collector.py

RUN chmod 755 thanos-store-garbage-collector.py

## Trigger script
CMD ["/usr/local/bin/python3", "/home/thanos-store-garbage-collector.py"]