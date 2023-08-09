FROM python:3.7.2-alpine3.8

WORKDIR /workDir

COPY . .

ENTRYPOINT ["python", "./workDir/fileMaker.py"]

VOLUME /workDir