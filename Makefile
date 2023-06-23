install:
	python -m poetry install

build-models:
	python -m poetry run datamodel-codegen --input data/cprt_schema.json --output cpyrt/models.py --class-name CPRT

clean:
	rm -rf dist
