build-models:
	python -m poetry run datamodel-codegen \
		--input data/cprt_schema.json \
		--output cpyrt/models.py \
		--class-name CPRTCoreModel

clean:
	rm -rf dist

install:
	python -m poetry install

test:
	python -m poetry run pytest
