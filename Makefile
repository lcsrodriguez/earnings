all:
	@echo "Installing the requirements"
	@python3 -m pip3 install -r requirements.txt

init:
	@echo "Creating output folders..."
	@mkdir -p "out"

install:
	@echo "Installing the requirements"
	@python3 -m pip3 install -r requirements.txt

clean:
	@echo "Cleaning output folders..."
	@rm -rf dist/ build/ out/ */*.egg-info *.egg-info

deploy-dev:
	@echo "Deploying (dev)..."
	@rm -rf dist/ build/
	@rm -rf */*.egg-info *.egg-info
	@python3 setup.py sdist bdist_wheel
	@twine upload --repository testpypi dist/*

deploy:
	@echo "Deploying (prod)..."
	@rm -rf dist/ build/
	@rm -rf */*.egg-info *.egg-info
	@python3 setup.py sdist bdist_wheel
	@twine upload dist/*
