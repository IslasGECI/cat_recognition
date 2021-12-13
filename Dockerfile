FROM python:3.8

WORKDIR /workdir
COPY . .

RUN apt-get update && apt-get install -y libgl1-mesa-dev ffmpeg libsm6 libxext6

RUN pip install \
    autopep8 \
    black \
    codecov \
    flake8 \
    h5py==2.10.0 \
    ipykernel \
    tensorflow==2.4.0 \
    keras-resnet==0.2.0 \
    keras==2.4.3 \
    matplotlib==3.3.2 \
    mutmut \
    numpy==1.19.3 \
    opencv-python \
    pillow==7.0.0 \
    pylint \
    pytest \
    pytest-cov \
    rope \
    scipy==1.4.1

RUN pip install imageai --upgrade