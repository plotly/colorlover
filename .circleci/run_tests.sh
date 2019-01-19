source activate colorlover_env
cd colorlover
nosetests -xv tests.py --with-coverage
mkdir ../artifacts/

if [ "$BUILD_COVERAGE_REPORT" = "1" ]
then
    coverage html -d ./coverage --title=$PYTHON_VERSION
    zip ../artifacts/coverage_$PYTHON_VERSION.zip coverage/*
fi
