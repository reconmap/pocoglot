
.PHONY: run
run:
	pocoglot/cli.py

.PHONY: prepare
prepare:
	pip install -r requirements.txt

.PHONY: build
build: prepare
	python3 -m build

.PHONY: release
release:
	python3 -m twine upload dist/*


