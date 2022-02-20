FROM gitpod/workspace-python

RUN export PATH="$(pyenv root)/shims:$PATH" && \
    pyenv install 3.9.10 && \
    pyenv global 3.9.10 && \
    pip3 install -r docs/requirements.txt

RUN brew install vale
