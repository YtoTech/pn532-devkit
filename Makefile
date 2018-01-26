install:
	pipenv install

serial-read-test:
	pipenv run python utils/test_serial.py
