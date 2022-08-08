#!/bin/bash
SCRIPT_LOC="$(dirname $(readlink -f ${BASH_SOURCE}))"

cd $SCRIPT_LOC/../docs && poetry run sphinx-apidoc -o . ..
cd $SCRIPT_LOC/../docs && make html
