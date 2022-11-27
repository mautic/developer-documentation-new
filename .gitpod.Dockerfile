FROM python:3.10

ENV VALE_VERSION=2.21.2

WORKDIR /workspace

# Needed for vale
RUN pip install rst2html

RUN mkdir -p vale && cd vale && wget https://github.com/errata-ai/vale/releases/download/v${VALE_VERSION}/vale_${VALE_VERSION}_Linux_64-bit.tar.gz && \
    tar -xf vale_${VALE_VERSION}_Linux_64-bit.tar.gz && cp /workspace/vale/vale /usr/local/bin/vale && cd ../

# /home/gitpod/.local/bin ensures that Python packages like rstcheck can be found
ENV PATH=/home/gitpod/.local/bin:$PATH

# Create the gitpod user. UID must be 33333. https://www.gitpod.io/docs/configure/workspaces/workspace-image#use-a-custom-dockerfile
RUN useradd -l -u 33333 -G sudo -md /home/gitpod -s /bin/bash -p gitpod gitpod

USER gitpod
