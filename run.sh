#!/usr/bin/env bash
#PBS -l nodes=1:ppn=28
#PBS -l walltime=24:00:00
#PBS -l pmem=1gb

cd $VSC_DATA/ParallelProgrammeren/projectTest6/ProjectParallelProgrammeren
# load necessary cluster modules and activate virtual environment
source micc-setup
# run python script
echo 'geparallelliseerd:'
mpiexec -n 28 python script3.py

echo 'niet geparallelliseerd:'
echo 'testen invloed aantal atomen in simulatie:'
python script.py
echo 'testen invloed aantal simulaties':
python script1.py
echo 'testen rng:'
python script2.py
