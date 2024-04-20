FROM alpine:latest

WORKDIR /app

COPY files /app/files

CMD find /app/files -type f -exec cat {} \; -exec echo \;