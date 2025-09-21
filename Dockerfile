FROM ubuntu:latest
LABEL authors="compu"

ENTRYPOINT ["top", "-b"]