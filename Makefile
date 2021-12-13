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
		linter \
		mutants \
		process_images \
		resize_images \
		setup \
		tests

check:
	black --check --line-length 100 ${module}
	black --check --line-length 100 tests
	flake8 --max-line-length 100 ${module}
	flake8 --max-line-length 100 tests

clean:
	rm --force --recursive ${module}.egg-info
	rm --force --recursive data/processed/*
	rm --force --recursive data/resized
	rm --force --recursive ${module}/__pycache__
	rm --force --recursive tests/__pycache__
	rm --force .mutmut-cache

coverage: setup
	pytest --cov=${module} --cov-report=xml --verbose && \
	codecov --token=${codecov_token}

format:
	black --line-length 100 ${module}
	black --line-length 100 src
	black --line-length 100 tests

linter:
	$(call lint, ${module})
	$(call lint, tests)

mutants:
	mutmut run --paths-to-mutate ${module}

tests:
	pytest --verbose

process_images: yolo.h5 resize_images src/first_recognition.py
	mkdir --parents data/processed
	python src/first_recognition.py

resize_images:
	python cat_recognition/resize_images.py

yolo.h5:
	wget https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5