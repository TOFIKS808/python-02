# Local development with venv

venv::
	python3 -m venv venv
.PHONY: venv

pip::
	pip install -r requirements.txt
	pip install -r requirements.dev.txt
PHONY: pip

lint::
	pylint src/ tests/ || true
.PHONY: lint

test::
	python  -m unittest discover tests -vvv
.PHONY: test

# Docker development
up::
	sudo chmod 777 volumes/data
	sudo chmod 777 volumes/backup
	$(MAKE) down || true
	docker-compose up -d
PHONY: up

enter::
	docker-compose exec anaconda /bin/bash
.PHONY: enter

down::
	docker-compose down
.PHONY: down

build::
	$(MAKE) down || true
	docker-compose rm -f || true
	docker-compose up --build -d
.PHONY: build

d-pip::
	docker-compose exec anaconda pip install --root-user-action=ignore -r requirements.txt
	docker-compose exec anaconda pip install --root-user-action=ignore -r requirements.dev.txt
.PHONY: d-pip

d-lint::
	docker-compose exec anaconda pylint src/ tests/
.PHONY: d-lint

d-test::
	docker-compose exec anaconda python -m unittest discover tests
.PHONY: d-lint


###########################
pop::
	python src/populate_db.py

d-pop::
	docker-compose exec anaconda python src/populate_db.py
