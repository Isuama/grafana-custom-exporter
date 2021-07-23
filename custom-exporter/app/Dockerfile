FROM python:3.6 as base
LABEL OWNER="Isuru Amarathunga"
WORKDIR /app
COPY dependencies.txt /app
RUN pip install --target=/app/dependencies -r ./dependencies.txt

FROM python:3.6
#ENV GROUP_ID=1000 USER_ID=1000
#RUN addgroup -g $GROUP_ID author
#RUN adduser -D -u $USER_ID -G author isuru -s /bin/sh
#USER isuru
RUN apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    net-tools \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY --from=base /app /app
COPY app.py /app
ENV PYTHONPATH="${PYTHONPATH}:/app/dependencies"
CMD ["python", "-u","app.py"]
