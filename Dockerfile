FROM python:3
WORKDIR /project
COPY . .
ENTRYPOINT [ "python3" "." ]