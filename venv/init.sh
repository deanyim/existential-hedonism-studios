#!/bin/bash

pip install virtualenvwrapper

export WORKON_HOME=~/.virtualenvs
mkdir -p $WORKON_HOME
source `which virtualenvwrapper.sh`
mkvirtualenv existential-hedonism-studios
workon existential-hedonism-studios
