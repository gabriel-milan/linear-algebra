clean:
	find . -type f -name '*.c' -delete
	find . -type f -name '*.so' -delete
	find . -type f -name '*.pyc' -delete
	rm -rf build/
	rm -rf dist/
	rm -rf btrader.egg-info/
build:
	python3 setup.py build_ext --inplace
install:
	python3 -m pip install .
uninstall:
	python3 -m pip uninstall alc
run_test:
	python3 test_array.py
