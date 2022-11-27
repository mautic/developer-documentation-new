FROM python:3.10

ARG VALE_VERSION=2.21.2

WORKDIR /workspace

RUN mkdir -p vale && cd vale && wget https://github.com/errata-ai/vale/releases/download/v${VALE_VERSION}/vale_${VALE_VERSION}_Linux_64-bit.tar.gz && \
    tar -xf vale_${VALE_VERSION}_Linux_64-bit.tar.gz && cd ../

# /home/gitpod/.local/bin ensures that Python packages like rstcheck can be found
# /workspace/vale ensures that Vale can be found
ENV PATH=/home/gitpod/.local/bin:/workspace/vale:$PATH
