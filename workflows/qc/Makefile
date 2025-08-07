.PHONY: all clean unittest
e2e:
	pytest -v -k "e2e" tests/
unittest:
	pytest -v -k "not e2e" tests/
