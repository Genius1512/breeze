#!/bin/bash
SCRIPT_LOC="$(dirname $(readlink -f ${BASH_SOURCE}))"
poetry run python3 $SCRIPT_LOC/../sandbox/main.py
