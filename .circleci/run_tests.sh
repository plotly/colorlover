cd colorlover
nosetests -xv tests.py --with-coverage
mkdir ../artifacts/
coverage html -d ./coverage --title=$PYTHON_VERSION
zip ../artifacts/coverage_$PYTHON_VERSION.zip coverage/*
