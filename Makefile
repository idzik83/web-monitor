requirements.txt: requirements.in
	pip-compile --output-file=requirements.txt requirements.in

requirements-dev.txt: requirements.in
	pip-compile --output-file=requirements-dev.txt requirements-dev.in
