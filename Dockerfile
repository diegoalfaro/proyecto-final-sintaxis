FROM python:3
WORKDIR /proyecto
COPY . .
WORKDIR /programas
VOLUME [ "/programas" ]
ENTRYPOINT [ "python3", "/proyecto" ]