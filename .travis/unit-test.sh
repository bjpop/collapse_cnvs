#!/bin/bash

set -e
errors=0

# Run unit tests
python collapse_cnvs/collapse_cnvs_test.py || {
    echo "'python python/collapse_cnvs/collapse_cnvs_test.py' failed"
    let errors+=1
}

# Check program style
pylint -E collapse_cnvs/*.py || {
    echo 'pylint -E collapse_cnvs/*.py failed'
    let errors+=1
}

[ "$errors" -gt 0 ] && {
    echo "There were $errors errors found"
    exit 1
}

echo "Ok : Python specific tests"
