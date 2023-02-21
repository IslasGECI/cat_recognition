all: mutants

module = cat_recognition
codecov_token = b29fe8aa-a6c6-4b4c-b54f-fe408af8fed0

define lint
	pylint \
        --disable=bad-continuation \
        --disable=missing-class-docstring \
        --disable=missing-function-docstring \
        --disable=missing-module-docstring \
        ${1}
endef

.PHONY: \
		all \
		check \
		clean \
		coverage \
		format \
		init \
		linter \
		mutants \
		process_images \
		resize_images \
		setup \
		tests

check:
	black --check --line-length 100 ${module}
	black --check --line-length 100 src
	black --check --line-length 100 tests
	flake8 --max-line-length 100 ${module}
	flake8 --max-line-length 100 src
	flake8 --max-line-length 100 tests


clean: clean_detections
	rm --force --recursive ${module}.egg-info
	rm --force --recursive ${module}/__pycache__
	rm --force --recursive build
	rm --force --recursive darknet
	rm --force --recursive data/processed/*
	rm --force --recursive data/resized
	rm --force --recursive dist
	rm --force --recursive tests/__pycache__
	rm --force --recursive .pytest_cache
	rm --force yolov3.weights
	rm --force .mutmut-cache

clean_detections:
	rm --force data/raw/photos/*
	rm --force --recursive data/resized

coverage: init resize_images yolo.h5
	pytest --cov=${module} --cov-report=xml --verbose && \
	codecov --token=${codecov_token}

format:
	black --line-length 100 ${module}
	black --line-length 100 src
	black --line-length 100 tests

init: setup tests

install_darknet:
	git clone https://github.com/pjreddie/darknet && cd darknet && make

linter:
	$(call lint, ${module})
	$(call lint, tests)

mutants: init resize_images
	mutmut run --paths-to-mutate ${module}

setup: install_darknet yolov3.weights
	mkdir --parents data/resized
	python setup.py install

tests:
	pytest --verbose -vv

process_images: setup yolo.h5 resize_images src/first_recognition.py
	mkdir --parents data/processed
	python src/first_recognition.py

resize_images:
	python src/resize_images.py

yolo.h5:
	wget https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5

yolov3.weights:
	wget --no-check-certificate https://pjreddie.com/media/files/yolov3.weights