
run:
	pocoglot/cli.py

prepare:
	pip install -r requirements.txt

build:
	python3 -m build

release:
	python3 -m twine upload dist/*


