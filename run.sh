#!/bin/bash

echo 'niet geparallelliseerd:'
python projectparallelprogrammeren/__init__.py
echo 'geparallelliseerd:'
mpiexec -n 6 python projectparallelprogrammeren/montecarlo_v3.py 
