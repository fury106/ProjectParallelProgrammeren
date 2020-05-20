#!/usr/bin/env bash
#PBS -l nodes=2:ppn=28
#PBS -l walltime=1:00:00
#PBS -l pmem=1gb

cd $VSC_DATA/ParallelProgrammeren/projectTest6/ProjectParallelProgrammeren
# load necessary cluster modules and activate virtual environment
source micc-setup
# run python script
echo 'geparallelliseerd:'
mpiexec -n 56 python script3.py
