FROM python:alpine

WORKDIR /workdir
COPY . .

RUN apt-get update && apt-get install -y libgl1-mesa-dev ffmpeg libsm6 libxext6

RUN pip install \
    autopep8 \
    black \
    codecov \
    flake8 \
    ipykernel \
    keras-resnet \
    keras \
    matplotlib==3.3.2 \
    mutmut \
    numpy \
    opencv-python \
    pillow \
    pylint \
    pytest \
    pytest-cov \
    rope \
    scipy \
    tensorflow \
    tqdm \
    typer \
    wandb

RUN make init
