all : distclean venv/bin/activate install

.PHONY: distclean
distclean :
	git clean -dx
	git reset --hard

venv/bin/activate :
	python3 -m venv venv

.PHONY: install
install : venv/bin/activate
	venv/bin/pip install --upgrade pip
	venv/bin/pip install --upgrade setuptools
	venv/bin/pip install -r requirements.txt

requirements.txt : venv/lib/python*/site-packages
	venv/bin/pip freeze > requirements.txt
